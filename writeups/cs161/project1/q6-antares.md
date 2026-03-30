# Antares — Format String Exploit with Two Half-Word Writes (CS161 Project 1)

## Objective
Exploit a format string vulnerability in the Antares targeting utility to redirect execution to attacker-controlled shellcode and read the protected `README` file.

---

## What Makes This Question Different

This question is not primarily about overflowing a buffer.  
Instead, it is about abusing a **format string vulnerability** in a `printf`-style call.

The prompt explicitly states that:

- `arg` is loaded into `argv`
- `env` is piped into standard input
- the shellcode is placed in `arg`
- the exploit uses a vulnerable `printf` call
- the attacker uses `%hn` to overwrite the saved return address in two halves

So the exploit pattern here is:

1. place shellcode somewhere predictable
2. locate its address
3. find a stack location we want to overwrite
4. use format string writes to change that location
5. redirect execution to shellcode

---

## High-Level Exploit Idea

The end goal is to overwrite the saved return address of the vulnerable function, likely `calibrate`, so that when the function returns it jumps into shellcode that we control.

The prompt tells us that the shellcode lives in `arg`, so the overall plan is:

1. place shellcode in `arg`
2. determine the shellcode address in memory
3. determine the saved RIP address of the vulnerable function
4. feed a malicious format string through the vulnerable `printf`
5. use `%hn` writes to patch the saved RIP so it becomes the shellcode address

---

## Vulnerability Class

This is a classic **format string vulnerability**.

A vulnerable pattern looks like:

```c
printf(buf);
```

instead of:

```c
printf("%s", buf);
```

If the attacker controls `buf`, then format specifiers such as:

- `%c`
- `%u`
- `%s`
- `%n`
- `%hn`

will be interpreted by `printf`.

This allows the attacker not only to read stack contents, but also to **write to memory** using `%n` or `%hn`.

---

## Why `%hn` Is Used Instead of `%n`

A full 32-bit address might be something like:

```text
0xbffff234
```

If we tried to write that using `%n`, we would need `printf` to have already printed the decimal value:

```text
3221226036
```

characters.

That is too large and would likely crash or hang the program.

So instead, the exploit splits the address into two 16-bit halves:

- lower half: `0xf234`
- upper half: `0xbfff`

Then we write them separately using `%hn`, which writes only 2 bytes.

That is why the prompt walks through an example like:

- write low half to `addr`
- write high half to `addr + 2`

This is the standard approach for 32-bit format string exploitation.

---

## Shellcode Placement

The prompt states that for this question:

> we place the shellcode in `arg`

So the attacker-controlled command-line argument contains the shellcode.

The first task is to find its exact memory address in GDB.

The prompt also gives a recognition hint:

> the shellcode itself should start with `0xcd58326a`

That means in GDB we should search for the bytes corresponding to the shellcode and identify its address precisely.

This address becomes the value we want to write into the saved return address.

---

## Vulnerable `printf` Call

The prompt says to locate the vulnerable `printf` call and break there.

That implies the actual exploit requires:

1. identifying where our controlled input sits relative to `printf`’s expected arguments
2. determining how many format specifiers are needed to walk up the stack
3. determining when `%hn` begins writing to attacker-controlled or chosen addresses

This is the heart of the exploit.

---

## Format String Mechanics

When `printf(buf)` is called:
- `buf` is treated as the format string
- `printf` expects additional arguments above it on the stack
- each format specifier consumes one of those arguments

Examples:

- `%c` consumes one argument and prints one character
- `%s` consumes one argument and dereferences it as a pointer
- `%n` consumes one argument as a pointer and writes the total bytes printed so far
- `%hn` does the same, but writes only 2 bytes

This gives the attacker two important abilities:

1. **skip stack slots**
2. **write controlled values to chosen addresses**

---

## Main Exploit Strategy

The likely exploit structure is:

### Part 1 — Put target addresses into attacker-controlled data
We need `printf` to eventually interpret some stack values as pointers to:
- saved RIP low half
- saved RIP high half

So we place those addresses somewhere that the format string can eventually reach.

### Part 2 — Walk up the stack
Use repeated format specifiers like `%c` or equivalent to consume stack arguments until `printf` reaches the attacker-controlled words.

### Part 3 — Print the correct number of characters
Use width-controlled output such as `%<k>u` to make the total printed byte count equal the 16-bit value we want.

### Part 4 — Use `%hn` twice
- first `%hn` writes the lower 16 bits of the shellcode address
- second `%hn` writes the upper 16 bits of the shellcode address

After that, the saved return address has been rewritten to point to shellcode in `arg`.

When the vulnerable function returns, execution jumps there.

---

## Why Two Writes Are Necessary

Suppose the shellcode address is:

```text
0xbffff234
```

Then the saved return address must become:

```text
34 f2 ff bf
```

in memory.

We cannot efficiently write all four bytes at once with `%n`, so we split it:

- write `0xf234` to `saved_rip`
- write `0xbfff` to `saved_rip + 2`

After both `%hn` writes, the saved return address becomes the shellcode address.

---

## Ordering Constraint

A subtle but important issue with `%hn` writes is that:

> the value written is the total number of characters printed so far

So the second write depends on the first.

That means we usually choose the order carefully:
- often write the smaller half first
- then print enough additional characters so the second total matches the larger half

If the second desired half is numerically smaller than the first, then wraparound behavior modulo `0x10000` may need to be used.

This is a standard detail in half-word format string exploits.

---

## Likely Structure of `arg` and `egg`

The prompt says the deliverables are two scripts, `egg` and `arg`.

Given the earlier statement that shellcode goes in `arg`, the likely division is:

### `arg`
Contains:
- shellcode
- possibly padding
- possibly addresses embedded for the format string exploit
- possibly the format string itself if the vulnerable program reads from `argv`

### `egg`
Provides:
- additional attacker-controlled input through standard input
- possibly the actual format string payload if the vulnerable buffer is read from stdin

The exact division depends on the source code, which is not shown here.

So one of the most important source-level questions is:

> which user-controlled channel actually reaches the vulnerable `printf` call?

---

## What I Would Look For in the Source

To finalize the exploit, I would inspect:

1. where `arg` is used
2. where `env` / stdin is used
3. which one becomes the argument to the vulnerable `printf`
4. where the saved RIP of `calibrate` is located
5. whether attacker-controlled addresses can be placed onto the stack near the format string
6. how many arguments need to be skipped before reaching those addresses

The exact exploit depends on those relationships.

---

## What I Would Determine in GDB

A complete exploit requires measuring:

1. **shellcode address**
   - where `arg` lands in memory

2. **saved RIP address**
   - address of the return address we want to overwrite

3. **stack offset**
   - how many format specifiers are needed before `printf` reaches our injected addresses

4. **write order**
   - lower-half then upper-half, or vice versa

5. **exact width values**
   - how many characters must be printed before each `%hn`

Without these measured values, a final exploit cannot be written reliably.

---

## Likely Vulnerability Description

The Antares program likely contains a format string vulnerability because it passes attacker-controlled input directly to `printf` as the format string. This allows an attacker to use `%hn` specifiers to write chosen values to arbitrary memory locations that appear as arguments on the stack. By carefully arranging pointers to the saved return address and printing controlled numbers of characters, the attacker can overwrite the low and high halves of the saved return address separately. The overwritten return address is set to the address of attacker-controlled shellcode stored in `arg`, causing execution to jump to that shellcode when the vulnerable function returns.

---

## Conservative Provisional Exploit Plan

1. Put shellcode in `arg`.
2. Run under GDB and find the shellcode address.
3. Break at the vulnerable `printf` call.
4. Draw the stack and identify the saved RIP of the vulnerable function.
5. Determine how to place:
   - `saved_rip`
   - `saved_rip + 2`
   onto the stack where `printf` will eventually consume them as arguments.
6. Determine how many stack arguments must be skipped.
7. Build a malicious format string that:
   - advances to the relevant stack positions
   - prints enough characters to reach the desired low-half value
   - uses `%hn`
   - prints enough additional characters to reach the desired high-half value
   - uses `%hn` again
8. Run the program.
9. When the function returns, control transfers to shellcode.
10. A shell appears, and `cat README` reveals the next credentials.

---

## Important Technical Details for the Final Version

A real final write-up will need to include:

- exact vulnerable source line
- exact shellcode address
- exact saved RIP address
- exact stack diagram at the vulnerable `printf`
- exact argument index where attacker-controlled addresses appear
- exact lower and upper halves written
- exact width values used before each `%hn`
- explanation of byte-count accumulation
- GDB evidence showing the saved RIP before and after the exploit

These should not be invented without the source or debugger output.

---

## Why the Shell Prompt May Look Strange

The prompt notes that the shell prompt:
- may require scrolling to see
- may not be aligned on the left side

That makes sense in a format string exploit because:
- the payload may print a large amount of padding or whitespace
- the terminal cursor may already be deep into the current line when the shell starts

So the odd shell prompt position is a side effect of the exploit itself.

---

## Likely Learning Goal

This question teaches:

- how format string vulnerabilities differ from buffer overflows
- how `%hn` can be used as a constrained write primitive
- how to transform a limited write primitive into full control-flow hijacking
- why controlling the number of printed characters matters
- how to split a 32-bit address into two 16-bit writes

This is a major conceptual step toward more general memory corruption exploitation.

---

## What I Can Say Reliably Right Now

Based on the prompt alone, the intended exploit is clearly:

> **place shellcode in `arg`, then use a format string vulnerability and two `%hn` writes to overwrite the saved return address with the shellcode address**

That is not speculative; it is directly supported by the step-by-step attack description in the question.

What remains unknown without the actual source or GDB output is:
- the exact stack layout
- the exact target address
- the exact format string payload
- the exact widths and skip counts

---

## Next Step

To turn this into a final write-up, the next required artifacts are:

- the vulnerable source code
- the measured shellcode address
- the measured saved RIP address
- the GDB stack diagram at the vulnerable `printf`

With those, the final write-up can include the exact format string payload and the precise sequence of two half-word writes.

# Vega — Off-by-One Exploit Using Environment Variable Shellcode (CS161 Project 1)

## Objective
Exploit the vulnerable Vega utility to execute attacker-controlled code and read the protected `README` file.

---

## What Makes This Question Different

This question changes the exploit model in two important ways:

1. The output of `egg` is stored as an **environment variable**
2. The output of `arg` is passed as a **command-line argument**

That means the exploit is split across two locations in memory:

- `egg` places attacker-controlled bytes high on the stack as an environment variable
- `arg` supplies the direct input to the vulnerable program through `argv`

This strongly suggests that the vulnerability is not a normal large overflow with inline shellcode.  
Instead, the exploit likely:
- places shellcode somewhere stable and attacker-controlled using `egg`
- uses the smaller or subtler corruption via `arg` to redirect control flow toward that shellcode

---

## Likely Vulnerability Class

The prompt explicitly points toward:
- Section 10 of “ASLR Smack & Laugh Reference”
- off-by-one vulnerabilities in the textbook

That is a very strong hint that this is an **off-by-one stack overflow**.

An off-by-one bug is weaker than a normal buffer overflow:
- you may not get full control over the saved return address directly
- you may only overwrite **one byte past the end** of a buffer

That sounds minor, but if that one byte lands on the **saved frame pointer (SFP)**, it can still be exploitable.

---

## Main Idea

The likely intended exploit is:

1. Use `egg` to place shellcode in an environment variable
2. Use `arg` to trigger an **off-by-one overwrite**
3. That overwrite changes the least significant byte of the saved frame pointer
4. When the function returns, the corrupted frame pointer causes stack unwinding to use attacker-influenced memory
5. Control flow is eventually redirected into shellcode stored in the environment

This is a classic “minor overwrite, major effect” scenario.

---

## Why the Environment Variable Matters

The prompt says the output of `egg` becomes an environment variable and is placed near the top of the stack.

That matters because:
- environment variables are attacker-controlled
- they can hold large payloads
- they can hold shellcode without needing to fit into the vulnerable local buffer
- their address can often be discovered in GDB

So the likely design is:

- `egg` = **where the shellcode lives**
- `arg` = **the trigger that corrupts stack state just enough to jump there**

This avoids the need to XOR or transform shellcode inline through the vulnerable input path.

---

## Why the SFP Is Probably the Target

The prompt contains a very revealing line:

> “There is a slight chance (1 in 256) that your VM customization causes the value of the SFP to end in \x00, which makes this question much harder to solve.”

That is a major clue.

If the least significant byte of the saved frame pointer matters, then the exploit probably relies on changing **only that final byte**.

That is exactly consistent with an off-by-one overwrite:
- buffer ends
- one extra byte is written
- that byte lands on the low byte of saved EBP / SFP

So the exploit does **not** directly overwrite RIP at first.  
Instead, it corrupts the saved frame pointer just enough that a later `leave; ret` sequence pivots the stack.

---

## Why This Can Still Lead to Code Execution

A normal function epilogue on x86 often behaves like:

```asm
leave
ret
```

Which is equivalent to:
1. `mov esp, ebp`
2. `pop ebp`
3. `ret`

If the saved frame pointer has been corrupted, then when the function unwinds:
- `esp` may be set to the wrong location
- the subsequent `pop` and `ret` may read values from attacker-controlled memory instead of the real stack frame

That means an off-by-one overwrite of SFP can cause:
- a **stack pivot**
- eventual control of the return path

This is why a single-byte overwrite can still be exploitable.

---

## Why the Müller Reference Is Relevant

The hint about “ASLR Smack & Laugh” suggests an exploit pattern where:
- shellcode is stored in environment memory
- control flow is redirected there indirectly

Even though ASLR is disabled here, the conceptual similarity is:
- use environment memory as a large, attacker-controlled landing zone
- use partial stack corruption to redirect execution into it

So the question is probably not about guessing addresses blindly, but about:
- finding the environment variable address in GDB
- constructing stack state so execution eventually reaches it

---

## Probable Vulnerability Shape

The likely bug is something like:
- a buffer used for case conversion
- a loop that writes one byte too many
- or a copy/termination bug that writes a null byte or transformed byte just beyond the buffer boundary

Example pattern:

```c
for (i = 0; i <= len; i++) {
    buf[i] = transform(input[i]);
}
```

instead of:

```c
for (i = 0; i < len; i++) {
    buf[i] = transform(input[i]);
}
```

Or:
- writing the terminator one byte past the end
- converting exactly one byte too many

This would make the bug subtle compared to earlier questions.

---

## Probable Exploit Structure

### Part 1 — `egg`
`egg` likely prints:
- shellcode
- possibly some padding
- possibly a NOP sled or equivalent landing area
- stored as an environment variable

The goal is to have a reliable, known address in memory that contains attacker-controlled executable bytes.

---

### Part 2 — `arg`
`arg` likely produces:
- a carefully sized argument
- long enough to fill the vulnerable buffer
- plus exactly **one extra byte**
- that last byte changes the low byte of the saved frame pointer

So `arg` is likely not a giant payload.  
It is likely precision-controlled.

---

## Likely Stack Effect

A likely stack layout is:

```text
[ local buffer ]
[ saved EBP / SFP ]
[ saved RIP ]
```

With an off-by-one, we probably only reach:

```text
[ local buffer ][ low byte of saved EBP ]
```

not the full return address.

That means the exploit path is probably:

1. overwrite low byte of saved EBP
2. function epilogue uses corrupted EBP
3. stack pointer moves into attacker-influenced region
4. subsequent `ret` reads attacker-controlled address
5. execution lands in environment shellcode

---

## What I Would Look For in the Source

To confirm the exact exploit, I would inspect:

1. the vulnerable buffer size
2. the copy or transform loop
3. whether the bug is:
   - loop bound error
   - terminator off-by-one
   - lower/upper-case conversion applied out of bounds
4. exact location of SFP relative to the buffer
5. whether the overflow writes:
   - a transformed character
   - a null byte
   - or one attacker-controlled byte

Those details determine how much control we truly have over the SFP byte.

---

## What I Would Look For in GDB

The prompt suggests using GDB to inspect `environ`.

I would want to determine:

1. the address of the environment variable containing `egg`
2. the exact bytes at that address
3. the address of the vulnerable buffer
4. the address of saved EBP / SFP
5. which byte of SFP is changed by the off-by-one
6. how that changed SFP affects the stack when the function returns

The essential measurements are:

- buffer start
- saved EBP address
- address of shellcode in environment
- resulting fake stack layout if any

---

## Why Address Drift Matters

The prompt warns that changing `egg` or `arg` may change addresses.

That makes sense because:
- argument strings
- environment variables
- stack layout

all affect final addresses on the process stack.

So the correct workflow is likely:

1. finalize `egg`
2. finalize `arg`
3. rerun GDB
4. re-measure addresses
5. only then build the final exploit

This is important because an exploit that was correct earlier may fail after even a small payload change.

---

## Why XOR Is Mentioned

The prompt says not to manually XOR anything longer than 4 bytes, and suggests using Python if needed.

That implies the vulnerable program may be transforming bytes in some way, likely through uppercase/lowercase conversion or a related operation.

So one possible constraint is:
- bytes passed through the vulnerable path are altered
- shellcode would be corrupted if sent directly that way

That is another reason to place shellcode in the environment instead:
- environment bytes can remain intact
- the command-line argument only needs to trigger control flow redirection

---

## Conservative Provisional Vulnerability Description

The Vega utility likely contains a stack-based **off-by-one** vulnerability in its case-conversion logic. Although the bug only overwrites one byte beyond the end of a local buffer, that byte appears to land on the least significant byte of the saved frame pointer. By carefully choosing that byte, an attacker can corrupt stack unwinding during the function epilogue. Instead of directly overwriting the return address, the exploit pivots control flow indirectly. Shellcode is stored separately in an environment variable, whose address can be discovered in GDB. The corrupted frame pointer then causes the function to return through attacker-influenced stack state, eventually transferring execution to the environment-resident shellcode.

---

## Conservative Provisional Exploit Plan

1. Write `egg` so it places shellcode in an environment variable.
2. Use GDB to locate the environment variable’s address.
3. Inspect the vulnerable function and determine:
   - buffer size
   - saved EBP address
   - exact off-by-one behavior
4. Build `arg` so it:
   - fills the buffer exactly
   - overwrites one extra byte
   - changes only the low byte of saved EBP in a useful way
5. Use GDB to observe the resulting stack frame after corruption.
6. Adjust until the function epilogue pivots execution toward attacker-controlled memory.
7. If successful, a shell appears and `cat README` reveals the next credentials.

---

## What the Final Write-Up Will Need

A complete final write-up should include:

- the exact source-level bug
- why it is off-by-one and not a larger overflow
- how the low byte of SFP is determined
- the exact address of the environment variable from GDB
- the exact relationship between corrupted SFP and control-flow redirection
- the final contents of `egg`
- the final contents of `arg`
- GDB evidence showing:
  - original SFP
  - corrupted SFP
  - location of shellcode
  - before/after stack behavior

Without the source or debugger output, those concrete values should not be invented.

---

## Likely Learning Goal

This question teaches that even a very small memory bug can still be exploitable.

More specifically, it demonstrates that:
- not all exploitation requires direct RIP overwrite
- frame-pointer corruption can be enough
- environment variables can provide a useful payload location
- subtle memory corruption can defeat seemingly minor defenses or constraints

This is a more realistic and more delicate exploitation pattern than the earlier large overflows.

---

## What I Can Say Reliably Right Now

Based on the prompt alone, the intended exploit is very likely:

- **not** a direct full overwrite of RIP
- **not** inline shellcode in the vulnerable input
- **not** simple brute force

It is much more likely:

> **environment-variable shellcode + off-by-one corruption of saved frame pointer**

That conclusion is strongly supported by:
- the off-by-one hint
- the SFP low-byte warning
- the environment-variable setup
- the Müller reference

---

## Next Step

To turn this into a full final write-up, the next required artifact is the actual vulnerable source code or relevant GDB output.

Once that is available, the final version should include:
- the exact bug
- the exact off-by-one offset
- the exact shellcode location in `environ`
- the exact SFP byte change
- the exact final `egg` and `arg` payloads

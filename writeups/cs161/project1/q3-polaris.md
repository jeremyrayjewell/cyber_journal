# Polaris — Stack Canary Bypass via Leak and Replay (CS161 Project 1)

## Objective
Exploit the vulnerable `dehexify` program on Polaris, bypass stack canaries, and execute the provided shellcode to print the next question’s credentials from `README`.

---

## What Makes This Question Different

This is the first question in the project that explicitly enables **stack canaries**.

A normal stack-smashing exploit would fail here because:
- overflowing the buffer also overwrites the canary
- when the function returns, the program checks whether the canary changed
- if the canary is different, the program aborts before using the overwritten return address

So the exploit must do two things at once:

1. **preserve the correct canary value**
2. **still overwrite the saved return address**

This means the problem is no longer just “find the offset and smash the stack.”  
We first need to **learn the canary**, then include it unchanged in the final payload.

---

## Vulnerable Program Behavior

The program `dehexify`:
- accepts text input
- interprets sequences like `\x41` as the corresponding byte `A`
- leaves non-hex escapes unchanged
- can process multiple inputs in one execution

Examples:
- input `\x41\x42` becomes `AB`
- input `XYZ` stays `XYZ`

This gives us a useful property:

> the program transforms user input before storing or printing it

That matters because it may let us:
- control the number of bytes written into memory
- affect where string termination occurs
- leak stack contents through output
- then send a second payload in the same execution

---

## Main Idea

The likely intended strategy is a **two-stage exploit**:

### Stage 1 — Leak the canary
Trigger the program to print stack bytes past the local buffer so that the canary becomes visible in output.

### Stage 2 — Replay the canary
Send a second payload that:
- overflows the buffer
- reinserts the exact leaked canary value unchanged
- overwrites saved frame data
- overwrites the return address with the address of our shellcode

This is why the question uses an `interact` script instead of a simple `egg` file:
- we must **receive program output**
- extract bytes from it
- use those exact bytes in the next input

---

## Why a Canary Leak Is Likely Possible

The prompt gives several clues:

- “You need to make sure the value of the canary isn’t changed when the function returns, but you still need to overwrite the RIP.”
- “You might want to save some C program output and input part of it back into the C program.”
- “No hex decoding or little-endian reversing is necessary to do this.”
- “You can decode multiple inputs within a single execution of a program.”

Those clues strongly imply:
- the canary is exposed by program output
- we can read it directly as raw bytes
- we can splice those exact bytes into a later payload
- the exploit is intentionally interactive

So the most likely vulnerability pattern is:

1. input causes the program to output memory beyond the intended string boundary
2. that output includes the canary
3. we capture the canary bytes
4. we reuse them in the final overflow payload

---

## Why the All-Random Canary Matters

The prompt notes that this project uses:
- **4 random bytes** for the canary

instead of the lecture convention:
- **3 random bytes + 1 NULL byte**

This matters because a NULL byte in a canary usually interferes with string-based leaks:
- printing as a C string often stops at `\0`

But in this project, the canary may contain no NULL at all, which makes it easier for the program to accidentally print it out as part of an unterminated string.

That strongly supports the idea that the intended bypass is an **information leak through string output**.

---

## Likely Vulnerability Pattern

The likely bug is:

1. user input is decoded into bytes
2. the decoded output is stored in a fixed-size stack buffer
3. the resulting string is printed unsafely or without proper termination
4. output extends past the end of the buffer into nearby stack memory
5. nearby stack memory includes the canary
6. the canary is leaked
7. attacker sends a second overflow that preserves the canary while overwriting RIP

This is not just a raw overflow.  
It is likely a combination of:

- **buffer overflow**
- **information disclosure**
- **canary replay**

---

## Probable Exploit Structure

The exploit likely has two sends.

### First input
Purpose:
- cause the program to echo or print memory past the end of the buffer
- capture the canary from output

Pseudo-flow:

```python
p.start()
p.send(first_input + '\n')
leak = p.recv(...)
```

Then extract the canary:

```python
canary = leak[start:end]
```

The exact slice depends on:
- buffer length
- how much output precedes the canary
- actual stack layout observed in GDB

---

### Second input
Purpose:
- perform the actual overflow
- include the original canary value unchanged
- overwrite the return address

Likely payload structure:

```text
[padding up to canary]
[leaked canary]
[padding over saved frame pointer]
[new RIP]
[shellcode or jump target]
```

Pseudo-flow:

```python
payload = (
    padding_to_canary +
    canary +
    padding_to_rip +
    new_return_address +
    SHELLCODE
)
p.send(payload + '\n')
```

---

## Why “No Little-Endian Reversing” Is Mentioned

The prompt specifically says:

> “No hex decoding or little-endian reversing is necessary to do this.”

That is a major hint.

It implies that the canary is not something we need to interpret numerically.  
We are supposed to:
- receive it as raw bytes
- preserve its exact byte order
- send it back exactly as received

So if the leaked bytes are:

```python
'\x12\x34\x56\x78'
```

we do **not** convert them to an integer and back.  
We just splice them directly into the next payload.

---

## Why the Function’s Extra Behavior Matters

The prompt also warns:

> “The function does not return immediately after the buffer overflow takes place ... so you will need to account for any extra behavior so that the stack is set up correctly when the function returns.”

This suggests that after the overflow:
- more code still runs
- that code may:
  - write more bytes
  - decode more input
  - append a null terminator
  - modify nearby stack contents

So the exploit cannot just overwrite RIP and assume immediate control.

We must understand:
- what instructions execute after the overflow
- whether those instructions clobber any part of our payload
- whether the stack must remain valid until function epilogue

This is why GDB is especially important here.

---

## What I Would Look For in `dehexify.c`

To finalize the exploit, I would inspect:

1. **buffer declaration**
   - size of local stack buffer

2. **decode loop**
   - how `\xNN` is transformed
   - whether output length differs from input length

3. **print logic**
   - is `printf("%s", buf)` used?
   - is termination guaranteed?

4. **stack canary placement**
   - relative offset of:
     - buffer
     - canary
     - saved EBP
     - saved RIP

5. **post-overflow behavior**
   - what happens after the copy/write
   - whether the function keeps processing bytes before returning

---

## What the Final Write-Up Will Need

A complete final write-up should include:

- exact vulnerability description
- how the canary leak works
- exact leaked bytes or GDB evidence showing where the canary is found
- exact offsets:
  - buffer start
  - canary location
  - saved RIP location
- exact payload structure
- explanation of how the final payload preserves the canary
- explanation of any adjustments needed because the function continues running after overflow

Without the source or debugger output, those exact values should not be invented.

---

## Conservative Provisional Vulnerability Description

The vulnerable `dehexify` program likely contains a stack-based buffer overflow but is protected by a stack canary. The intended bypass is probably to first leak the canary through unsafe output behavior, likely caused by improper string termination after dehexification. Because the canary can be observed in program output, an attacker can capture its raw bytes and include them unchanged in a second overflow payload. This preserves the canary check while still overwriting the saved return address and redirecting control flow to attacker-controlled shellcode.

---

## Conservative Provisional Exploit Plan

1. Start the program with `p.start()`.
2. Send an input designed to trigger an output leak.
3. Read the program’s output with `p.recv(...)` or `p.recvline()`.
4. Extract the canary bytes from the leaked output.
5. Build a second payload containing:
   - padding up to canary
   - the exact leaked canary bytes
   - filler for saved frame pointer
   - overwritten return address
   - shellcode
6. Send the second payload.
7. Let the function return normally with the canary intact.
8. The shellcode prints `README`.

---

## Likely Learning Goal

This question is teaching that modern mitigations do not eliminate exploitation.  
Instead, they change the workflow:

- first leak protected state
- then preserve that state in the final payload
- then redirect execution anyway

So the important conceptual shift is:

> a mitigation like a stack canary is only effective if the attacker cannot learn and replay its value

---

## What I Can Say Reliably Right Now

Based on the prompt alone, the intended solution is very likely:

- **not** brute-force
- **not** bypassing the canary by skipping the check
- **not** smashing the stack blindly

It is much more likely:

> **leak canary → replay canary → overwrite RIP**

That conclusion is strongly supported by the interact API, the hints about saving output, and the note that the canary contains four random bytes.

---

## Next Step

To turn this into a full real write-up, the next required artifact is the actual `dehexify.c` source or GDB output.

Once that is available, the final version should include:
- the precise bug
- the exact leak method
- the exact canary slice
- the exact offset to RIP
- the exact final interact payload

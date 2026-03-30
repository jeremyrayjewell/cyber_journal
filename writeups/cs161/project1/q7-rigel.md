# Rigel — Defeating ASLR and Stack Canaries with a Probabilistic Exploit (CS161 Project 1)

## Objective
Exploit the Rigel binary despite both **stack canaries** and **ASLR** being enabled, and execute the provided shellcode to print the final credentials from `README`.

---

## What Makes This Question Different

This is the final and hardest challenge in the project because it combines the two major mitigations introduced earlier:

- **stack canaries**
- **ASLR (Address Space Layout Randomization)**

Earlier questions isolated these ideas:
- Polaris focused on canary bypass
- Antares and Vega involved control-flow redirection techniques
- Rigel now combines mitigation bypass with address uncertainty

The prompt also explicitly says the solution may be **nondeterministic**, and that `./exploit` runs multiple times to account for this.

That strongly implies the intended exploit is **probabilistic**, not perfectly deterministic.

---

## Defensive Situation

At this point, the target has:

### 1. Stack canary protection
A direct overflow that corrupts the canary will fail before the function returns.

### 2. ASLR
Important addresses vary between executions, so we cannot rely on fixed addresses for:
- stack buffers
- shellcode
- saved return targets
- other useful code/data locations

### 3. NX disabled
The prompt says CSA allies disabled non-executable pages on the remote system.

That matters because:
- injected shellcode can still execute if we can redirect control flow to it
- this is not a ROP-only problem
- the remaining challenge is not “how to execute code,” but “how to land on the right address without violating the canary”

---

## Main Exploit Problem

To succeed, the exploit must do both:

1. **preserve or correctly replay the stack canary**
2. **redirect execution to shellcode despite address randomization**

So the challenge is not just memory corruption.

It is:

> **reliable-enough control-flow hijacking under uncertainty**

---

## Likely Intended Strategy

The prompt specifically directs the student to Section 8.1 of *ASLR Smack & Laugh Reference* and notes that this exploit was not discussed in lecture.

That strongly suggests the intended solution is some variation of:

- place shellcode in a region of memory we partially control
- create a large landing region or NOP sled
- redirect execution to an address guess that is not exact
- rely on repeated attempts until one lands correctly
- preserve the stack canary along the way

So the exploit is likely:

> **canary bypass + partial address guess + NOP sled + repeated runs**

---

## Why a NOP Sled Is Relevant

The prompt explicitly reminds us:

> a no-op instruction in assembly can be represented by the single-byte instruction `0x90`

That is a major hint.

A NOP sled allows the exploit to tolerate imprecision in the final jump address.

Instead of needing to jump to the exact first byte of shellcode, we can jump to a region like:

```text
[NOP][NOP][NOP][NOP][shellcode]
```

If execution lands anywhere in the sled, it slides forward into the shellcode.

This is especially useful when ASLR makes exact targeting impossible.

---

## Probabilistic Nature of the Exploit

The prompt says:

- `./exploit` runs five times
- segmentation faults are expected
- success only needs to happen once

That implies the exploit probably does **not** recover a full exact randomized address at runtime.

Instead, it likely:
- narrows the possible address range
- guesses a useful address within that range
- relies on repeated execution and a sufficiently large sled to eventually succeed

This is consistent with classic stack-ASLR bypasses when:
- the entropy is limited
- stack layout is somewhat stable
- attacker-controlled data occupies a broad area

---

## Likely Role of the Interact Script

This question uses an `interact` file rather than simple static payload generation.

That suggests the exploit may need to:
- receive output first
- preserve all printed bytes carefully
- respond dynamically
- possibly leak or replay some protected value
- possibly synchronize with program I/O before sending the final payload

The prompt specifically warns:

> it is necessary to receive all bytes that are printed out to you to prevent errors

That strongly suggests the exploit depends on correctly tracking the program’s full output stream, likely because:
- output contains important leaked data
- or missing bytes causes the script to desynchronize from program execution

So the `interact` script is probably not optional complexity.  
It is central to the exploit.

---

## Likely Canary Bypass Component

Since stack canaries are enabled, the exploit likely still requires a step similar to Polaris:

- leak the canary value somehow
- preserve it in the final payload
- overflow past it without changing it

The challenge text does not spell out the leak method, but given the overall project progression, the likely pattern is:

1. leak stack state or otherwise recover the canary
2. construct the final payload including the correct canary bytes
3. continue past the canary to overwrite control data

Without that, any direct stack-smashing payload would be detected and terminated.

So even though ASLR is the new headline challenge, **canary handling remains mandatory**.

---

## Likely Combined Exploit Structure

A plausible high-level structure is:

### Stage 1 — Obtain or preserve canary
The exploit must learn or preserve the current canary value.

### Stage 2 — Place shellcode in a reachable randomized region
Likely on the stack or in attacker-controlled input.

### Stage 3 — Prefix shellcode with a NOP sled
This creates tolerance for imperfect address targeting.

### Stage 4 — Overflow the vulnerable buffer
The payload must:
- fill the buffer
- include the correct canary unchanged
- overwrite saved control-flow data

### Stage 5 — Use an approximate jump target
Instead of an exact address, choose a guessed address likely to land somewhere inside the sled.

### Stage 6 — Repeat until one run succeeds
Because ASLR changes the address, repeated runs are expected to eventually hit.

---

## Why Disassembly Matters

The prompt suggests using:

```gdb
disas <function_name>
```

That likely matters because the exploit may need to understand:
- exact function epilogue behavior
- exact call sequence
- locations of useful instructions
- whether a return address overwrite needs to target:
  - shellcode directly
  - or a nearby instruction sequence

Even if the final exploit jumps to shellcode, disassembly is often needed to understand:
- stack layout near the vulnerable function
- how much post-overflow code executes before return
- whether there are any stable in-function targets

---

## Likely Vulnerability Shape

Because the prompt does not emphasize a new logic flaw or format string issue, the core vulnerability is probably still a memory corruption bug such as:
- stack buffer overflow
- unsafe copy
- inadequate bounds checking

But unlike earlier questions, the exploit cannot rely on:
- exact static addresses
- direct inline overwrite without mitigation handling

So the vulnerability itself may be conceptually simpler than the exploit technique required to weaponize it.

---

## What I Would Look For in the Source

To finalize the exploit, I would inspect:

1. the vulnerable buffer and copy path
2. the exact stack frame layout
3. where the canary sits relative to the buffer
4. how output may leak memory or stack data
5. where the shellcode ends up in memory
6. how large a NOP sled can be placed
7. whether the overwritten return address must target:
   - the shellcode region directly
   - or another useful address on the stack

---

## What I Would Measure in GDB

A final exploit would need real measurements for:

1. **canary position and value**
2. **buffer start**
3. **distance from buffer to canary**
4. **distance from canary to saved RIP**
5. **approximate address range of attacker-controlled shellcode**
6. **how much that address varies across runs**
7. **how large a NOP sled can be used**
8. **whether the guessed return address should target the middle of the sled**

That last point is important: with ASLR, we usually do not aim at the beginning of the sled. We aim near the middle of the likely landing zone to maximize success probability.

---

## Likely Exploit Philosophy

This question is probably teaching a specific idea:

> when exact addresses are unavailable, make precision less necessary

That is what the NOP sled does.

And alongside that:

> mitigations stack, so the exploit must satisfy all of them simultaneously

That is what preserving the canary while tolerating ASLR uncertainty accomplishes.

---

## Conservative Provisional Vulnerability Description

The Rigel program likely contains a memory corruption vulnerability that would normally allow stack-based code execution. However, exploitation is complicated by both stack canaries and ASLR. The attacker must preserve the stack canary to survive the integrity check and then redirect execution to shellcode without knowing its exact address in advance. Because NX is disabled, injected shellcode can still execute if reached. The intended bypass is likely probabilistic: a payload containing the correct canary, a large NOP sled, and shellcode is placed in memory, and the saved return address is overwritten with an approximate guess into that region. Repeated runs are expected until ASLR causes the guess to land within the sled, after which execution slides into the shellcode.

---

## Conservative Provisional Exploit Plan

1. Start the program with the interact script.
2. Read all program output carefully using `p.recvline()` to avoid desynchronization.
3. Determine how the canary can be obtained or preserved.
4. Build a payload containing:
   - padding up to the canary
   - the correct canary bytes
   - padding to the saved return address
   - a guessed return address into a large sled
   - a NOP sled (`0x90` bytes)
   - the provided shellcode
5. Send the payload through the correct input channel.
6. Allow the program to run.
7. If the guessed address lands inside the sled, execution reaches the shellcode and prints `README`.
8. If not, the run may segfault; repeat until one attempt succeeds.

---

## Why `recvline()` Is Probably Important

The prompt explicitly recommends `p.recvline()` over `p.recv(n)`.

That suggests:
- line-oriented output matters
- counting bytes manually is error-prone
- consuming too little output may leave unread bytes in the stream
- unread bytes could desynchronize the later send/receive sequence

So part of the exploit is not just memory corruption, but **correct I/O discipline**.

---

## What the Final Write-Up Will Need

A complete final write-up will need:

- the actual vulnerable source code
- precise explanation of how the canary is handled
- exact payload layout
- how the guessed return address was chosen
- where the shellcode and NOP sled are placed
- whether the shellcode is in the stack, argument, or another attacker-controlled region
- measurements or observations about ASLR spread
- explanation of why the exploit is probabilistic
- execution evidence showing at least one successful run

Without the source or debugger output, those exact implementation details should not be fabricated.

---

## Likely Learning Goal

This final question is designed to show that:

- mitigations increase exploit complexity but do not automatically make exploitation impossible
- stack canaries protect against naive overwrites, but not against exploits that can preserve them
- ASLR weakens exact targeting, but can be partially overcome with probabilistic landing and a NOP sled
- modern exploitation often combines:
  - information recovery
  - payload layout strategy
  - control-flow redirection
  - reliability engineering

This is the transition from “single bug exploitation” to “mitigation-aware exploitation.”

---

## What I Can Say Reliably Right Now

Based on the prompt alone, the intended exploit is very likely:

> **preserve the canary, then use a NOP sled and a probabilistic address guess to land in shellcode despite ASLR**

That conclusion is strongly supported by:
- the coexistence of canaries and ASLR
- the note that repeated runs and segfaults are expected
- the explicit reminder about `0x90`
- the reference to the ASLR Smack & Laugh material

What remains unknown without the source or debugging output is:
- the exact vulnerability
- the exact canary leak/replay mechanism
- the exact shellcode location
- the exact guessed address strategy
- the exact final `interact` payload

---

## Next Step

To convert this into a full final write-up, the next required artifacts are:

- the vulnerable source code
- debugger observations of the stack layout
- confirmation of where the shellcode is placed
- confirmation of how the canary is obtained or preserved
- measurements showing the randomized address range across runs

With those, the final version can include the exact exploit structure and the logic behind the guessed return target.

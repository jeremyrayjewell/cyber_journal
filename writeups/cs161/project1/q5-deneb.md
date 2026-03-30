# Deneb — Error-Handling Vulnerability and File Overwrite (CS161 Project 1)

## Objective
Exploit the Deneb file utility to bypass its improved security checks and execute the provided shellcode to retrieve the next credentials.

---

## What Makes This Question Different

This question shifts focus away from pure memory corruption and toward:

> **logical vulnerabilities in error handling**

Unlike earlier questions:
- this may not rely on classic buffer overflow
- the vulnerability is likely in how the program **handles failure cases**

The prompt explicitly asks:

> “What security vulnerabilities occur during error checking?”

So the goal is to identify:
- where validation is performed
- how failures are handled
- whether the program still proceeds in an unsafe state

---

## Relevant Security Concepts

This question is directly tied to:

- Fail-safe defaults (deny by default)
- Complete mediation (always check access)

Common violations include:
- continuing execution after a failed check
- assuming an operation succeeded when it did not
- using invalid or uninitialized values after an error

---

## Likely Vulnerability Pattern

Based on the description (“more secure version of Spica file viewer”):

The program likely:
1. reads a file or filename
2. performs a validation check
3. attempts to open or process the file
4. handles errors incorrectly

A common flawed pattern is:

```c
if (check_fails) {
    printf("error\n");
}
process_file(...);
```

Instead of:

```c
if (check_fails) {
    return;
}
```

So even if validation fails:
- execution continues
- unsafe operations still occur

---

## Likely Exploit Strategy

The prompt gives a major hint:

> “example code also provides an example of how to overwrite files”

So the exploit likely involves:

> **causing the program to overwrite a file it should not control**

Most likely target:
- overwrite `README`
- or overwrite a file that is later executed or read with elevated privileges

---

## Main Idea

The intended vulnerability is probably:

1. validation checks attempt to restrict file access
2. those checks fail under certain conditions
3. the program continues execution anyway
4. file operations occur with unintended parameters
5. attacker gains control over file contents or behavior

This is a violation of:

- fail-safe defaults → system should stop on failure
- complete mediation → checks must apply to every access

---

## Role of the Interact Script

Unlike earlier questions, this uses an `interact` script, which suggests:

- multiple inputs and outputs
- dynamic behavior based on program responses
- possibly:
  - reading output
  - then sending new input based on that output

So the exploit likely requires:

1. triggering an error condition
2. observing how the program responds
3. using that state to influence a later operation

---

## Likely Exploit Flow

A plausible high-level sequence:

1. Start the program
2. Provide input that causes a validation failure
3. Observe that the program continues execution anyway
4. Trigger a file operation using attacker-controlled input
5. Cause a file overwrite (e.g., overwrite `README`)
6. The program later executes or reads the modified file
7. The provided shellcode prints the credentials

---

## Why Multiple Runs Are Allowed

The success condition says:

> “The exploit will run three times… as long as it passes at least once”

This suggests:
- the exploit may be unreliable or probabilistic
- timing or state conditions may vary
- the vulnerability may depend on:
  - race-like behavior
  - partial initialization
  - non-deterministic conditions

So a correct exploit may not succeed every run.

---

## What I Would Look For in the Source

To confirm the vulnerability, I would inspect:

1. all validation checks
   - filename checks
   - length checks
   - permission checks

2. how errors are handled
   - does the program return or continue?
   - are error values ignored?

3. file operations
   - `open`, `read`, `write`
   - whether attacker input controls file paths

4. any mismatch between:
   - what is validated
   - what is actually used

---

## Likely Vulnerability Types

Based on the prompt, likely candidates include:

- TOCTOU-style issues (time-of-check vs time-of-use)
- improper error handling
- unchecked return values
- file descriptor misuse
- fallback logic that is unsafe

---

## Conservative Provisional Vulnerability Description

The Deneb utility likely attempts to enforce stricter validation than previous challenges but contains flaws in its error-handling logic. Specifically, the program may detect invalid input or a failed operation but continue execution instead of terminating safely. This allows subsequent file operations to proceed using attacker-controlled or invalid state. As a result, an attacker can manipulate file behavior, potentially overwriting sensitive files or triggering unintended execution paths, ultimately allowing the provided shellcode to run.

---

## Conservative Provisional Exploit Plan

1. Start the program using the interact script
2. Trigger a validation failure condition
3. Observe program output and behavior
4. Identify whether execution continues after failure
5. Use subsequent input to:
   - control file paths or file contents
   - trigger a write operation
6. Overwrite a sensitive file or influence execution flow
7. Allow the program to execute shellcode
8. Verify that credentials are printed

---

## What the Final Write-Up Will Need

To complete a full write-up, the following must be confirmed using source code and GDB:

- exact validation logic and where it fails
- exact condition under which execution continues incorrectly
- specific file operation used in the exploit
- exact inputs sent in each step of the interact script
- before/after program state demonstrating the flaw
- evidence of file overwrite or unintended execution

Without the source, exact details should not be fabricated.

---

## Likely Learning Goal

This question teaches that:

- security is not just about memory safety
- logic errors can be just as dangerous
- error handling must enforce safe termination
- validation is meaningless if execution continues afterward

In particular:

> detecting an error is not enough — the system must also respond correctly to that error

---

## What I Can Say Reliably Right Now

Based on the prompt alone, the exploit is very likely:

- not primarily about buffer overflow
- not purely about memory layout
- but about **incorrect handling of failure states leading to unsafe file operations**

---

## Next Step

To finalize this write-up, the actual vulnerable program source is required.

With that, the final version should include:
- precise vulnerability location
- exact exploit interaction sequence
- exact file manipulation performed
- concrete evidence from execution or debugging

# Pen-Testing Experiments & Scripts

A quick overview of the tools and scripts used in this repository:

* **cipher-graphs/**: Visualizations of cryptographic algorithms.
* **generate\_ssh\_summary/**: SSH automation tool that reads `~/ssh-logs` and writes a summary to `~/ssh-summary.md`.
* **nofiltergpt-chat/**: Records of chatbot experiments.

---

## SSH Summary Generator

A simple utility to turn raw SSH debug logs into a Markdown table.

**To run:**

```bash
cd experiments/generate_ssh_summary
chmod +x generate_ssh_summary.py
./generate_ssh_summary.py
cat ~/ssh-summary.md
```

---

## Author

**Jeremy Ray Jewell**
[GitHub](https://github.com/jeremyrayjewell) | [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)

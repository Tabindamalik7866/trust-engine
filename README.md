 Trust Engine 🛡️
An automated Security-as-Code platform that detects and remediates vulnerabilities in Python code.

 The Problem
Manual code review doesn't scale. As AI-generated code floods repositories, security vulnerabilities like SQL Injection and hardcoded secrets are slipping into production.

 The Solution
Trust Engine uses Python's `ast` (Abstract Syntax Tree) module to perform deep static analysis.
- Detects: Risks like hardcoded keys and SQL injection.
- Remediates: Automatically rewrites code to use secure patterns.
- Audits: Generates machine-readable `audit_report.json` files.
  
 How to run
1. Clone the repo.
3. Place your code in the directory.
4. Run `python forge_engine.py` to audit and harden your project.

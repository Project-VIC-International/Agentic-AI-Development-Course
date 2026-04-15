# Cybersecurity, NIST & CJIS Compliance

---

## Your Tools Handle Sensitive Data

Any tool you build for CAC investigations will handle:

- **Criminal Justice Information (CJI)** — regulated by the FBI CJIS Security Policy
- **Personally Identifiable Information (PII)** — suspect, victim, and witness data
- **Evidence** — digital artifacts with chain of custody requirements
- **Law Enforcement Sensitive (LES)** information

Security is not optional. It's a legal requirement.

---

## DOJ CJIS Security Policy

The FBI's [CJIS Security Policy](https://www.fbi.gov/services/cjis/cjis-security-policy-resource-center) defines security requirements for any system that accesses, stores, or transmits Criminal Justice Information.

**Key requirements for your tools:**

| Area | Requirement |
|------|------------|
| Access Control | Authentication, authorization, role-based access |
| Encryption | Data encrypted at rest AND in transit — always |
| Auditing | Log who accessed what, when |
| Personnel Security | Background checks for anyone with access |
| Media Protection | Secure handling of storage devices |
| Physical Security | Controlled access to systems and data |
| Incident Response | Plan for security breaches |
| Configuration Management | Track changes to systems and software |

**Your agent can help.** Point the agent at the CJIS Security Policy and ask it to generate a compliance checklist for your tool.

---

## Encryption at All Times

This is the simplest and most critical security control:

### Data at Rest
- All stored data must be encrypted
- Use AES-256 or equivalent
- This includes databases, files on disk, backups, and USB drives

### Data in Transit
- All network communication must be encrypted
- Use TLS 1.2+ for all connections
- No unencrypted HTTP — always HTTPS
- VPN for remote access to agency systems

### Key Management
- Encryption keys must be stored securely
- Keys must be rotated regularly
- Never hardcode keys in source code

---

## NIST Cybersecurity Framework & 800-53

### NIST Cybersecurity Framework

The [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework) provides a structured approach:

**Five functions:** Identify → Protect → Detect → Respond → Recover

Use this as your security planning template.

### NIST SP 800-53: Security Controls

[NIST SP 800-53](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final) defines comprehensive security and privacy controls. It is organized into control families:

| Family | What It Covers |
|--------|---------------|
| AC — Access Control | Who can access what |
| AU — Audit & Accountability | Logging and monitoring |
| CM — Configuration Management | Managing system changes |
| IA — Identification & Authentication | Proving identity |
| SC — System & Communications Protection | Encryption, network security |
| SI — System & Information Integrity | Protecting data accuracy |

### NIST Cybersecurity Overlays

Overlays customize the NIST 800-53 controls for specific missions. **Law enforcement and CJIS have specific overlays** that tell you which controls apply to your environment and at what level.

---

## How the Agent Helps You With Security

You don't need to memorize these standards. **Point your agent at them.**

> "Read the CJIS Security Policy and generate a security requirements checklist for a Python tool that processes CyberTip data and stores it in a graph database."

> "Review my application against NIST 800-53 control family AC (Access Control) and tell me what I'm missing."

> "Add encryption at rest using AES-256 to the database connection in my tool."

**The agent reads the standards, understands the requirements, and helps you implement them.** All you have to do is point it at the right documents and ask.

---

## The Constitution Handles This

Remember the project constitution from spec-driven development?

Your constitution should include:

- **CJIS Security Policy compliance** as a mandatory requirement
- **NIST 800-53 control baseline** appropriate for your environment
- **Encryption requirements** (at rest and in transit)
- **Testing and validation requirements** before operational deployment

When the agent builds your tool from the spec, it inherits these security requirements automatically. Security is built in from the start, not bolted on at the end.

---

## Bottom Line

| Do This | Not This |
|---------|----------|
| Encrypt everything, always | "We'll add encryption later" |
| Reference CJIS in your constitution | Ignore security standards |
| Use NIST 800-53 as your control framework | Make up your own controls |
| Point your agent at the standards | Try to memorize every control |
| Test security before deployment | Assume the agent got it right |

# Security Policy

## ⚠️ Important Scope Distinction

Please distinguish between vulnerabilities in the **OpenMac directory repository** and vulnerabilities in **third-party open-source applications** listed within the directory:

1. **Third-Party Application Vulnerabilities**:
   - If you discover a security vulnerability in software listed in OpenMac (e.g. VLC, Bitwarden, IINA, etc.), **do not report it here**.
   - Please report it directly to the upstream security team of that specific project via their respective GitHub Security Advisories, security policies, or official contact addresses.

2. **OpenMac Repository & Automation Security**:
   - This policy applies strictly to security concerns affecting the OpenMac repository itself, including:
     - CI/CD workflows and automated GitHub Actions (`.github/workflows/`)
     - Python scripts (`scripts/validate-projects.py`, `scripts/generate-readme.py`, etc.)
     - Malicious project links, misleading redirects, or typo-squatted repositories submitted to `data/projects.yml`
     - Cross-site scripting (XSS) or injection vectors within generated Markdown or SVG assets.

---

## 🔒 Reporting a Vulnerability in OpenMac

If you discover a security issue or malicious submission within this repository:

1. **Do not disclose the issue publicly** in an open issue, discussion, or pull request.
2. Please utilize [GitHub Private Vulnerability Reporting](https://github.com/shareefmx/OpenMac/security/advisories/new) on this repository.
3. Provide a clear description of the vulnerability, proof of concept, and affected files.

### Response Timeframes
- **Initial Acknowledgment**: Within 48 hours.
- **Triage and Impact Assessment**: Within 5 business days.
- **Remediation & Advisory Release**: Resolved as quickly as possible, coordinated with the reporter.

---

## 🛡️ Supply Chain & Malicious Listing Prevention

OpenMac implements automated defenses to prevent malicious repository additions:
- **Canonical URL verification**: Enforces HTTPS and hosted Git endpoints (GitHub, GitLab, Codeberg).
- **Automated duplicate checks**: Prevents misleading repository clones from overriding established tools.
- **Manual maintainer audit**: Every submitted repository is verified for authentic upstream ownership and release pedigree prior to merging.


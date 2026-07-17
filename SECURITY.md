<div align="center">

# 🛡️ Security Policy
### CardioShield & Machine Learning Journey Diagnostics Security

</div>

---

## ℹ️ Policy Overview
As this repository documents an educational journey and diagnostic tools, we take code security, dependency hygiene, and model integrity seriously. This security policy outlines the supported versions, reporting processes, and security recommendations when working with the serialization tools in this project.

---

## 📦 Supported Versions

We currently support and patch only the latest release version or active commits on our main branch.

| Version | Supported |
| :--- | :---: |
| **Latest (main branch)** | ✅ Active |
| **Legacy Releases** | ❌ Not Supported |

---

## 🎯 Security Scope

Please report vulnerabilities affecting the core repository features:
1. **Dependency Vulnerabilities:** Outdated packages in `requirements.txt` with known CVEs (e.g., in `scikit-learn`, `pandas`, `FastAPI`).
2. **Data & Credential Exposure:** Accidentally committed API keys, credentials, or private diagnostic logs within Jupyter notebooks.
3. **Model Deserialization Risks:** Insecure model load implementations. 

> [!WARNING]
> **Pickle Warning:** This project uses serialized Python `.pkl` files (via `pickle`) for production deployment. Python's `pickle` module is **not secure** against erroneous or malicious data. Never load untrusted models from unknown sources as they can execute arbitrary code during deserialization.

---

## ✉️ Reporting a Vulnerability

If you discover a security vulnerability, please do **not** open a public GitHub issue. Instead, report it privately using one of the following methods:

1. **GitHub Private Vulnerability Reporting:**
   * Go to the repository homepage on GitHub.
   * Click on the **Security** tab.
   * Click **Advisories** in the left sidebar.
   * Click **Report a vulnerability** to submit a private report.

2. **Email Communication:**
   * Contact the maintainer directly via email. *(You can find the contact details on the GitHub Profile Page)*.

### ⏱️ Our Response Commitment
* **Initial Assessment:** Within **48 hours** of report receipt.
* **Resolution/Patching:** We aim to release a patch or package version update within **7 to 14 days** depending on vulnerability severity.

---

## 🛠️ Security Best Practices for Users
When cloning and playing with these machine learning notebooks:
* Always run the virtual environment isolated from your global system environment (`python -m venv venv`).
* Keep your dependencies up to date by regularly running `pip install --upgrade -r requirements.txt`.
* If you generate model artifacts using your own data, ensure the output `.pkl` files are kept in secure, restricted-access directories.

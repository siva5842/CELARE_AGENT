# 🛡️ Celare: Enterprise PII Detector & Masker

**Team Name:** Kinetic Prism  
**Challenge:** AI Prototype Challenge (Local PII Masking Agent)  

## 📖 Problem Statement
Accidental leaks of Personally Identifiable Information (PII) in enterprise datasets pose significant compliance and security risks. Celare provides a local-first, highly secure application designed to scan, detect, and mask sensitive Indian PII data (Emails, Phones, PAN, Aadhaar) without transmitting data to external cloud APIs.

## 🏗️ Architecture Overview
Celare utilizes a **2-Phase Hybrid Processing Engine**:
1. **Phase 1 (Deterministic Engine):** High-speed regex processing via `pandas` to instantly identify and redact structured Indian PII formats, replacing them with dynamic structural masks (e.g., `42YYYYYYYY12`).
2. **Phase 2 (Contextual AI Agent Loop):** A local `llama3.2` instance running via Ollama that scans soft, unstructured text strings. It utilizes a deterministic confidence-scoring loop, reprompting itself up to 3 times to validate context before applying redactions.

## 🚀 Tech Stack
* **Language:** Python
* **Data Processing:** `pandas`
* **Local AI Engine:** Ollama (`llama3.2`)
* **Frontend:** Streamlit
* **Testing:** `pytest`

## ⚙️ 1-Click Setup (Windows)
We have fully automated the deployment process for ease of evaluation.
1. Double-click the `setup.bat` file to automatically install dependencies and launch the app.

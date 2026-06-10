# Celare: Enterprise PII Detector & Masker

A local-first, highly secure data protection application built in Python. The system reads enterprise datasets (CSV, JSON, XLSX), scans for Personally Identifiable Information (PII), and applies dynamic structural masking. It utilizes a **2-Phase Hybrid Engine**—combining high-speed deterministic Regex for structured data with a **Contextual Agent Loop** (powered by a local Llama 3.2 model via Ollama) to validate unstructured "soft PII" without ever transmitting sensitive data to the cloud.

Built by **Team Kinetic Prism** for the AI Prototype Challenge.

---

## Features

* **2-Phase Hybrid Processing Engine**:
* *Phase 1:* High-speed Pandas/Regex engine that instantly redacts structured Indian PII (Emails, 10-digit Phones, PAN, Aadhaar).
* *Phase 2:* Local Ollama Agent Loop that reads unstructured text (like support notes), scoring extraction confidence and reprompting itself to validate context before masking.


* **Dynamic Structural Masking**: Generates unique, randomized replacement symbols per run while preserving structural formatting (e.g., masking an Aadhaar card as `12YYYYYYYY12` or a PAN card as `AXXXXXXXK`).
* **Modern Interactive Dashboard**: A sleek, reactive single-page web dashboard built with Streamlit, featuring drag-and-drop ingestion, interactive side-by-side data rendering, and session history tracking.
* **Robust Data Pipeline**: Automatically cleans data ingestion errors, stripping Pandas float artifacts from phone numbers and utilizing negative lookbehinds to catch spaced/hyphenated IDs.
* **Multi-Format Export**: Natively ingests and exports data across `.csv`, `.json`, and `.xlsx` formats while providing a downloadable Verification Report detailing masking metrics.
* **100% Local Execution**: Completely isolated execution environment ensuring zero data leakage to external APIs.
* **1-Click Windows Setup**: Includes an automated batch script that autonomously downloads Ollama, pulls the Llama 3.2 model, builds the virtual environment, and launches the app.

---

## Folder Structure

```text
Celare/
│
├── sample_data/            # Input folder containing mock enterprise datasets
│   ├── mock_dataset.csv
│   └── expected_masked_output.csv
│
├── app.py                  # Streamlit frontend, UI layout, and routing
├── data_ingestion.py       # Multi-format Pandas file reading/writing logic
├── regex_engine.py         # Phase 1 Deterministic Engine (Structural Masking)
├── llm_engine.py           # Phase 2 Contextual Engine (Ollama Agent Loop)
├── run_tests.py            # Verification runner
├── test_pii.py             # Pytest suite for masking validation
├── setup.bat               # 1-click automated Windows installer and launcher
├── requirements.txt        # Python dependency list
├── logo.png                # Project branding asset
├── AI_USAGE_NOTE.md        # Official AI Pair-Programming logs and prompts
└── README.md               # Project documentation

```

---

## Installation Steps

### Option A: 1-Click Automated Setup (Windows)

1. **Clone the Repository**:
```bash
git clone https://github.com/siva5842/CELARE_AGENT.git
cd CELARE_AGENT

```


2. **Run the Installer**:
Double-click the `setup.bat` file. The script will autonomously check for Ollama, download the `llama3.2` model, create a virtual environment, install all Python dependencies, and launch the dashboard in your browser.

### Option B: Manual Setup (macOS/Linux/Windows)

1. **Clone the Repository**:
```bash
git clone https://github.com/siva5842/CELARE_AGENT.git
cd CELARE_AGENT

```


2. **Set up a Virtual Environment**:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

```


3. **Install Dependencies**:
```bash
pip install -r requirements.txt

```


4. **Initialize Local AI Engine**:
Ensure Ollama is installed (from ollama.com), then pull the required model:
```bash
ollama pull llama3.2

```



---

## Usage Instructions

Run the Streamlit orchestrator script:

```bash
python -m streamlit run app.py

```

On execution, the script will spin up a local server and **automatically open the web dashboard** in your default web browser (typically on `http://localhost:8501`).

### Interactive Dashboard Walkthrough

* **File Ingestion**: Drag and drop your dataset (up to 200MB) into the prominent bottom-anchored upload zone. The engine automatically detects header formats and bypasses row-skipping bugs.
* **Data Preview**: View your raw dataset side-by-side against the newly structurally masked dataset.
* **Analytics Visualization**: Review the auto-generated green bar charts and metric counters tracking the exact distribution of masked entities (Emails, Phones, PAN, Aadhaar).
* **Multi-Format Export**: Use the dropdown menu at the bottom of the screen to select your preferred output format (CSV, JSON, XLSX) and click download to securely retrieve your sanitized file alongside the Verification Report.
* **Run History**: Navigate to the History tab to view chronological logs of your previous masking sessions.

---

### 🎥 Project Demonstration

[![Watch the Celare Demo](Project/logo.png)](https://drive.google.com/file/d/1tK7n_jcHjGx-AUChx6UQiT2BYilu-AQy/view?usp=drivesdk)

*Click the logo above to watch the full Celare demonstration on Google Drive.*



## Sample Input and Output

### Sample Input Data (`sample_data/mock_dataset.csv`)

```csv
id,name,email,phone,pan,aadhaar,notes
1,Rajesh Kumar,rajesh.k@example.com,9876543210,ABCDE1234F,1234 5678 9012,Contact rajesh.k@example.com for queries

```

### Processed Output Record (After 2-Phase Engine Execution)

```csv
id,name,email,phone,pan,aadhaar,notes
1,[REDACTED_NAME],####@example.com,98******10,AXXXXXXXF,12YYYYYYYY12,Contact ####@example.com for queries

```

*(Note: Symbols `*`, `X`, `#`, `Y` are randomized uniquely upon every execution session).*

---

## Future Enhancements

1. **OCR Document Processing**: Integrate PyTesseract to extract and mask PII from scanned PDFs and image-based invoices.
2. **Global Regex Expansion**: Expand the deterministic engine beyond Indian frameworks to recognize international identifiers (SSN, EU VAT numbers, Global Passports).
3. **Role-Based Access Control (RBAC)**: Implement a login layer where basic users can only download masked data, while admin users can view the unmasked source tables.
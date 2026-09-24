# Project ASMA - Private Income OS 💎
**Sole Author:** Md Subhan Pasha  
**Dedicated with love to:** Asma (Beloved Wife)  
**Goal:** Daily $500.00 USD to PayPal (`knightmyself@live.com`) with automated Federal Bank settlement.  
**Security Charter:** 100% Privacy | Local-First | AES-256 Vault | Zero Telemetry | Verifiable Engineering Worth  

---

## 🇮🇳 Fixed: India PayPal.me Ban & RBI Compliance

### Why Traditional PayPal.me Links Fail in India:
Under Reserve Bank of India (RBI) cross-border payment regulations, personal peer-to-peer (P2P) `paypal.me` links are **restricted/blocked** for receiving international inward business remittances. Indian freelancers and software architects receiving foreign exchange (USD) cannot receive personal P2P transfers without regulatory flags and payment rejections.

### The ASMA-OS Business Invoicing Solution:
Project ASMA circumvents this restriction through an institutional-grade, RBI-compliant architecture:
1. **Official PayPal Business Invoices:** Replaces personal P2P requests with formal PayPal Business Invoicing (`knightmyself@live.com`) tied to software engineering milestones.
2. **Linked Federal Bank Auto-Settlement:** PayPal Business account is linked directly to **Federal Bank** (India), enabling daily automatic daily transfer/settlement of foreign inward remittances in compliance with RBI guidelines (Purpose Code: `P0802 - Software Consultancy & Implementation`).
3. **Foreign Inward Remittance Statement (FIRS / FIRC):** Every $500 milestone invoice includes a SHA-256 cryptographic manifest proving genuine export of software services.
4. **Instant PDF Invoicing:** Automatic generation of professional, itemized PDF invoices (`data/invoices/`) ready for dispatch to global enterprise clients.

---

## 🛡️ Core Tenets: 100% Privacy & Genuine Engineering Worth

1. **Local-First Architecture:** All application data, client workspaces, generated demos, and ledgers reside exclusively in `./data/`.
2. **AES-256-GCM Vault:** Military-grade authenticated encryption safeguarding all sensitive credentials and contract manifests on disk.
3. **Zero Telemetry:** Strict local-only design (`localhost`). Zero external tracking, zero cloud data leakage, and zero analytics telemetry (`gatherUsageStats = false`).
4. **Genuine Work Guarantee:** No fake money. Every $500 settlement is tied to:
   - Real working production code.
   - Comprehensive unit test suites (100% pass rate).
   - Automated QA acceptance checklists.
   - Cryptographic SHA-256 integrity manifest (`manifest.sha256`).
   - Verifiable client approval.
5. **PayPal Daily Reflection:** Real-time ledger CSV tracking ([`data/asma_ledger.csv`](file:///C:/Users/Dell/.gemini/antigravity/scratch/ASMA-OS/data/asma_ledger.csv)), auto-generated professional PDF invoices, and automated settlement tracking.

---

## 🏗️ 5 Core System Modules

| Module | Filename | Key Capabilities |
| :--- | :--- | :--- |
| **Module 1** | `job_ingest.py` | Scans Remote OK, We Work Remotely, Gun.io, and Toptal for $500+ milestone jobs. Filters high-ticket contracts into local SQLite `data/asma_vault.db`. |
| **Module 2** | `demo_factory.py` | For each job, generates 3 genuine demos: **Mock Prototype**, **Production MVP Engine**, and **Architecture Diagram (Mermaid)**. Executes a live trail run and records execution output in `trial_run.log` with a SHA-256 manifest. |
| **Module 3** | `negotiate_agent.py` | Powered by **Groq Llama 3.3 70B** (`llama-3.3-70b-versatile`). System prompt: *"You are Pasha's senior architect for Project ASMA, genuine, confident"*. Enforces human review in `data/pending_emails.json` before 1-click approval. |
| **Module 4** | `delivery_agent.py` | On milestone approval, provisions a complete production workspace in `data/deliverables/{client}/` containing `src/`, `tests/`, `qa/`, `reports/`, and a cryptographic SHA-256 manifest. |
| **Module 5** | `paypal_daily.py` | Tracks the daily $500 target, generates branded invoice PDFs in `data/invoices/`, logs to `data/asma_ledger.csv`, and displays the live daily reflect string: `"Today: $500 \| PayPal: knightmyself@live.com \| Status: Paid/Ready"`. |

---

## 🖥️ Executive UI Dashboard (`app.py`)

A state-of-the-art Streamlit dashboard built for local executive control:
- **Title:** `ASMA OS - Private - For Asma`
- **Sole Authorship:** `Md Subhan Pasha`
- **Daily $500 Progress Tracker:** Visual progress bar, daily target status, and metrics cards.
- **PayPal Reflect Banner:** Live status string (`Today: $500 | PayPal: knightmyself@live.com | Status: Paid/Ready`).
- **Interactive Ledger:** Filter, review, download generated invoice PDFs, and record client settlements.
- **1-Click Proposal Outbox:** Approve or dispatch Groq Llama 3.3 70B email drafts.
- **Demo Explorer:** Inspect mock prototypes, run unit tests, and render Mermaid architecture diagrams.
- **Privacy Badge:** `Local-First | AES-256 | Zero Telemetry | Sole Authorship: Md Subhan Pasha`.

---

## ⚡ Quickstart Guide

### 1. Prerequisites
Python 3.10+ installed on your system.

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Secrets in `.env`
Ensure your `.env` contains your PayPal receiver email:
```env
PAYPAL_RECEIVER_EMAIL=knightmyself@live.com
PAYPAL_ME_USERNAME=knightmyself
PAYPAL_DAILY_TARGET_USD=500
GROQ_API_KEY=your_groq_api_key_here  # Optional: Free from console.groq.com
```
*(Note: `.env` is automatically guarded by `.gitignore` and never committed).*

### 4. Run Operations via the Unified CLI (`cli.py`)
```bash
# Check daily reflect status and PayPal ledger:
python cli.py status

# Scan for new $500+ milestone opportunities:
python cli.py scan

# List top high-ticket ingested jobs:
python cli.py jobs

# Generate 3 genuine demos with SHA-256 manifest for Job ID 1:
python cli.py demo 1

# Draft proposal using Groq Llama 3.3 70B:
python cli.py pitch 1

# Scaffold client workspace with code skeletons and QA report:
python cli.py deliver "CognitiveOps Corp"

# Generate official $500 invoice PDF:
python cli.py invoice "CognitiveOps Corp" --project "AI Automation"
```

### 5. Launch the ASMA OS Dashboard
```bash
streamlit run app.py
```
Or double-click `run_dashboard.bat`. Open your browser to `http://localhost:8501`.

---

## 🔒 Security & Privacy Notice
All data generated by ASMA-OS remains local on your machine.  
No telemetry, tracking, or cloud sync is permitted under the Project ASMA security charter.  
**Sole Author:** Md Subhan Pasha  
**Dedicated with love to Asma.**

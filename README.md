# 🏥 DRGMaster Enterprise: Inpatient Coding & DRG Optimization Platform

An enterprise-grade multi-page Streamlit application designed for clinical documentation, inpatient case structuring, DRG validation, physician query workflows, and financial analytics.

---

## 🚀 Project Overview & Phases

This platform fulfills the complete 4-week internship engineering and medical coding curriculum:

* **Phase 1: Inpatient Case Structuring (`1_Single_Patient.py`)**
  * Captures admission, discharge, and length of stay (LOS) data.
  * Models principal diagnoses, secondary diagnoses, and surgical procedures with severity/risk indicators.

* **Phase 2: DRG Assignment Support & Batch Processing (`2_Batch_Processing.py`)**
  * Maps coded data to Diagnosis-Related Group (DRG) groupers.
  * Highlights MCC/CC (Major Complication/Comorbidity) impacts on case weights and estimated reimbursement.
  * Bulk CSV/Excel validation engine with error tracking and instant report downloads.

* **Phase 3: Clinical Documentation Review Hooks (`3_Documentation_Query.py`)**
  * Identifies documentation gaps for DRG-impacting conditions.
  * Routes queries to attending physicians for clinical clarification.
  * Maintains an interactive query-response audit trail.

* **Phase 4: Financial and Quality Analytics (`4_Financial_Analytics.py`)**
  * Tracks departmental Case-Mix Index (CMI) trends.
  * Analyzes revenue variance from DRG corrections.
  * Monitors DRG denials and rebill success rates.

---

## 📁 Directory Structure

```text
drgmaster-internship/
├── app.py                      # Main landing page & configuration
├── requirements.txt            # Project dependencies
├── SUMMARY.md                  # Executive project report
└── pages/
    ├── 1_Single_Patient.py     # Week 1: Inpatient Case Intake & DRG Mapping
    ├── 2_Batch_Processing.py   # Week 2: Bulk CSV/Excel Validation Engine
    ├── 3_Documentation_Query.py # Week 3: Physician Query & Audit Workflow
    └── 4_Financial_Analytics.py # Week 4: CMI Trends & Revenue Variance
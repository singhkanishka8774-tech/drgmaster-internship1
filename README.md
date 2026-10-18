# 🏥 DRGMaster Enterprise: Inpatient Coding & DRG Optimization Platform

An enterprise-grade multi-page Streamlit application designed for clinical documentation, inpatient case structuring, DRG validation, physician query workflows, and financial analytics[span_0](start_span)[span_0](end_span)[span_1](start_span)[span_1](end_span).

---

## 🚀 Project Overview & Phases

This platform fulfills the complete 4-week internship engineering and medical coding curriculum[span_2](start_span)[span_2](end_span)[span_3](start_span)[span_3](end_span):

* **Phase 1: Inpatient Case Structuring (`1_Single_Patient.py`)**[span_4](start_span)[span_4](end_span)[span_5](start_span)[span_5](end_span)
  * Captures admission, discharge, and length of stay (LOS) data[span_6](start_span)[span_6](end_span)[span_7](start_span)[span_7](end_span).
  * Models principal diagnoses, secondary diagnoses, and surgical procedures with severity/risk indicators[span_8](start_span)[span_8](end_span)[span_9](start_span)[span_9](end_span).
* **Phase 2: DRG Assignment Support & Batch Processing (`2_Batch_Processing.py`)**[span_10](start_span)[span_10](end_span)[span_11](start_span)[span_11](end_span)
  * Maps coded data to Diagnosis-Related Group (DRG) groupers[span_12](start_span)[span_12](end_span)[span_13](start_span)[span_13](end_span).
  * Highlights MCC/CC (Major Complication/Comorbidity) impacts on case weights and estimated reimbursement[span_14](start_span)[span_14](end_span)[span_15](start_span)[span_15](end_span).
  * Bulk CSV/Excel validation engine with error tracking and instant report downloads.
* **Phase 3: Clinical Documentation Review Hooks (`3_Documentation_Query.py`)**[span_16](start_span)[span_16](end_span)[span_17](start_span)[span_17](end_span)
  * Identifies documentation gaps for DRG-impacting conditions[span_18](start_span)[span_18](end_span)[span_19](start_span)[span_19](end_span).
  * Routes queries to attending physicians for clinical clarification[span_20](start_span)[span_20](end_span)[span_21](start_span)[span_21](end_span).
  * Maintains an interactive query-response audit trail[span_22](start_span)[span_22](end_span)[span_23](start_span)[span_23](end_span).
* **Phase 4: Financial and Quality Analytics (`4_Financial_Analytics.py`)**[span_24](start_span)[span_24](end_span)[span_25](start_span)[span_25](end_span)
  * Tracks departmental Case-Mix Index (CMI) trends[span_26](start_span)[span_26](end_span)[span_27](start_span)[span_27](end_span).
  * Analyzes revenue variance from DRG corrections[span_28](start_span)[span_28](end_span)[span_29](start_span)[span_29](end_span).
  * Monitors DRG denials and rebill success rates[span_30](start_span)[span_30](end_span)[span_31](start_span)[span_31](end_span).

---

## 🗂️ Directory Structure

```text
drgmaster-internship/
│
├── app.py                      # Main landing page & configuration
├── requirements.txt            # Project dependencies
├── SUMMARY.md                  # Executive project report
└── pages/
    ├── 1_Single_Patient.py     # Week 1: Inpatient Case Intake & DRG Mapping
    ├── 2_Batch_Processing.py   # Week 2: Bulk CSV/Excel Validation Engine
    ├── 3_Documentation_Query.py# Week 3: Physician Query & Audit Workflow
    └── 4_Financial_Analytics.py# Week 4: CMI Trends & Revenue Variance
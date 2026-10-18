# 🏥 Project Summary Report: DRGMaster Enterprise Platform

**Project Title:** DRGMaster – Inpatient Coding & DRG Optimization Tool  
**Domain:** Medical Coding & Health Informatics  
**Environment:** Python, Streamlit, Pandas  

---

## Executive Overview
The **DRGMaster Enterprise Platform** is a multi-page health informatics web application designed to optimize inpatient coding accuracy, validate Diagnosis-Related Group (DRG) assignments, manage Clinical Documentation Integrity (CDI) query workflows, and provide executive-level financial analytics.

---

## 📅 Timeline & Deliverables Summary

### Week 1: Inpatient Case Structuring & Intake (`1_Single_Patient.py`)
* **Core Objective:** Capture patient admission, discharge, and length of stay (LOS) data.
* **Key Functionality:** Interactive clinical intake form calculating LOS dynamically, modeling principal diagnoses (ICD-10-CM), and assigning baseline DRGs.

### Week 2: DRG Mapping & Batch Processing (`2_Batch_Processing.py`)
* **Core Objective:** Bulk processing and DRG validation logic.
* **Key Functionality:** High-volume CSV/Excel file batch upload engine, evaluating comorbidity (CC/MCC) severity tiers, calculating relative weights, estimating reimbursements, and providing error logs with downloadable CSV reports.

### Week 3: Clinical Documentation Query Workflow (`3_Documentation_Query.py`)
* **Core Objective:** Identify documentation gaps and establish CDI workflows.
* **Key Functionality:** Automated detection of suspected unconfirmed conditions (e.g., Sepsis, AKI), physician query routing, and an interactive query-response audit log tracking clinical updates.

### Week 4: Financial & Quality Analytics (`4_Financial_Analytics.py`)
* **Core Objective:** Enterprise-wide revenue integrity and quality metrics.
* **Key Functionality:** Executive dashboard tracking Case-Mix Index (CMI) trends across clinical departments, revenue variance from DRG corrections, and DRG denial/rebill recovery metrics.

---

## 🛠️ Key Technical Accomplishments
1. **Modular Architecture:** Structured as a multi-page Streamlit application with a central landing dashboard (`app.py`) and discrete phase modules located in the `pages/` directory.
2. **State Management:** Utilized Streamlit `session_state` to maintain persistent audit history and query tracking across user interactions.
3. **Data Integrity & Exporting:** Enabled instant data parsing via Pandas and automated export capabilities for processed batch claims and CDI audit logs.
import streamlit as st
import pandas as pd
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="DRGMaster: Enterprise DRG Mapping Engine",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 DRGMaster: Enterprise DRG Mapping & Validation Engine")
st.subheader("Week 1: Single Patient Inpatient Intake & Core DRG Grouping")
st.markdown("---")

BASE_RATE = 6500.00

DRG_DATABASE = {
    "I21.9": {
        "mdc": "MDC 05: Diseases & Disorders of the Circulatory System",
        "base_drg": "282",
        "title": "Acute Myocardial Infarction",
        "weights": {"Base": 0.9850, "CC": 1.1200, "MCC": 1.4500}
    },
    "J44.9": {
        "mdc": "MDC 04: Diseases & Disorders of the Respiratory System",
        "base_drg": "192",
        "title": "Chronic Obstructive Pulmonary Disease",
        "weights": {"Base": 0.7200, "CC": 0.9100, "MCC": 1.2800}
    },
    "E11.9": {
        "mdc": "MDC 10: Endocrine, Nutritional & Metabolic Diseases",
        "base_drg": "638",
        "title": "Diabetes w/o CC/MCC",
        "weights": {"Base": 0.6500, "CC": 0.8500, "MCC": 1.1500}
    }
}

CC_CODES = ["E11.69", "N18.3", "I50.9"]
MCC_CODES = ["I50.21", "N18.6", "J96.00", "R57.0"]

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📋 Patient & Encounter Info")
    patient_id = st.text_input("Patient ID", "PT-10024")
    encounter_id = st.text_input("Encounter ID", "ENC-9982")
    adm_date = st.date_input("Admission Date", datetime.now())
    dis_date = st.date_input("Discharge Date", datetime.now())
    los = (dis_date - adm_date).days
    los = max(los, 1)
    st.info(f"Calculated Length of Stay (LOS): **{los} Day(s)**")

with col2:
    st.markdown("### 🔍 Clinical Coding Intake")
    principal_icd = st.selectbox(
        "Principal Diagnosis Code (ICD-10-CM)",
        options=list(DRG_DATABASE.keys())
    )
    sec_icd_input = st.text_input(
        "Secondary Diagnoses (comma-separated)",
        "I50.21, E11.69"
    )
    procedure_code = st.text_input("Surgical Procedure Code (Optional)", "")

st.markdown("---")

if st.button("⚡ Run DRG Mapping & Calculate Reimbursement", type="primary"):
    sec_codes = [code.strip().upper() for code in sec_icd_input.split(",") if code.strip()]
    has_mcc = any(code in MCC_CODES for code in sec_codes)
    has_cc = any(code in CC_CODES for code in sec_codes)
    
    if has_mcc:
        severity_tier = "MCC"
    elif has_cc:
        severity_tier = "CC"
    else:
        severity_tier = "Base"
        
    drg_info = DRG_DATABASE.get(principal_icd)
    
    if drg_info:
        rel_weight = drg_info["weights"][severity_tier]
        est_reimbursement = rel_weight * BASE_RATE
        
        st.success("✅ DRG Grouping Successfully Calculated!")
        
        res_col1, res_col2, res_col3, res_col4 = st.columns(4)
        res_col1.metric("Assigned MDC", drg_info["mdc"].split(":")[0])
        res_col2.metric("MS-DRG Code", f"{drg_info['base_drg']} ({severity_tier})")
        res_col3.metric("Relative Weight", f"{rel_weight:.4f}")
        res_col4.metric("Est. Reimbursement", f"${est_reimbursement:,.2f}")
        
        st.json({
            "Patient ID": patient_id,
            "Encounter ID": encounter_id,
            "Principal Diagnosis": f"{principal_icd} - {drg_info['title']}",
            "Secondary Diagnoses": sec_codes,
            "Severity Tier": severity_tier,
            "Reimbursement": f"${est_reimbursement:,.2f}"
        })
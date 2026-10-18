import streamlit as st
import pandas as pd
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="DRGMaster: Single Patient",
    page_icon="👤",
    layout="wide"
)

st.title("🏥 DRGMaster: Enterprise DRG Mapping Engine")
st.subheader("Week 1: Single-Patient DRG Mapping Module")
st.markdown("---")

BASE_RATE = 6500.00

DRG_DATABASE = {
    "I21.9": {
        "mdc": "MDC 05: Diseases and Disorders of the Circulatory System",
        "base_drg": "282",
        "title": "Acute Myocardial Infarction",
        "weights": {"Base": 0.95, "MCC": 1.45, "CC": 1.15}
    },
    "J18.9": {
        "mdc": "MDC 04: Diseases and Disorders of the Respiratory System",
        "base_drg": "195",
        "title": "Pneumonia, Unspecified Organism",
        "weights": {"Base": 0.72, "MCC": 1.20, "CC": 0.95}
    },
    "E11.9": {
        "mdc": "MDC 10: Endocrine, Nutritional and Metabolic Diseases",
        "base_drg": "638",
        "title": "Type 2 Diabetes Mellitus without Complications",
        "weights": {"Base": 0.55, "MCC": 0.98, "CC": 0.75}
    },
    "K57.92": {
        "mdc": "MDC 06: Diseases and Disorders of the Digestive System",
        "base_drg": "392",
        "title": "Diverticulitis of Intestine",
        "weights": {"Base": 0.68, "MCC": 1.10, "CC": 0.88}
    }
}

st.sidebar.header("📋 Patient Clinical Inputs")
patient_id = st.sidebar.text_input("Patient Identifier", value="PT-100924")
primary_icd = st.sidebar.selectbox("Primary Diagnosis (ICD-10 Code)", list(DRG_DATABASE.keys()))
severity = st.sidebar.radio("Complication Level", ["Base", "CC", "MCC"], help="CC: Complication/Comorbidity, MCC: Major CC")

st.header("📊 DRG Analysis Results")

if primary_icd in DRG_DATABASE:
    data = DRG_DATABASE[primary_icd]
    weight = data["weights"][severity]
    est_reimbursement = BASE_RATE * weight

    col1, col2, col3 = st.columns(3)
    col1.metric("Assigned Base DRG", f"DRG-{data['base_drg']}")
    col2.metric("Relative Weight", f"{weight:.2f}")
    col3.metric("Est. Reimbursement", f"${est_reimbursement:,.2f}")

    st.markdown("### Clinical Details")
    st.write(f"**Patient ID:** `{patient_id}`")
    st.write(f"**Major Diagnostic Category (MDC):** {data['mdc']}")
    st.write(f"**DRG Description:** {data['title']} ({severity})")
else:
    st.error("ICD-10 Code not found in database.")
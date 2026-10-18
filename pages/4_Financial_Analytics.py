import streamlit as st
import pandas as pd

st.set_page_config(page_title="Financial & Quality Analytics", layout="wide", page_icon="📈")

st.header("📈 Phase 4: Financial and Quality Analytics")
st.caption("Week 4: Case-Mix Index Trends, Revenue Variance, and DRG Denial Tracking")

# --- Top Level Key Metrics ---
st.subheader("📊 Key Performance Indicators (KPIs)")
m1, m2, m3, m4 = st.columns(4)

m1.metric("Overall Case-Mix Index (CMI)", "1.84", "+0.12")
m2.metric("Total Revenue Variance", "$142,500", "+$18,200")
m3.metric("DRG Denial Rate", "3.2%", "-0.8%")
m4.metric("Rebill Success Rate", "88.5%", "+2.1%")

st.divider()

# --- Section 1: Departmental CMI Trends ---
st.subheader("1. Case-Mix Index Trends by Department")

cmi_data = pd.DataFrame({
    "Department": ["Cardiology", "Pulmonology", "Gastroenterology", "Orthopedics", "Neurology"],
    "Total Cases": [320, 210, 180, 250, 140],
    "Average CMI": [2.15, 1.68, 1.45, 1.92, 1.78],
    "Target CMI": [2.00, 1.60, 1.40, 1.85, 1.70]
})

st.dataframe(cmi_data, use_container_width=True)

st.divider()

# --- Section 2: Revenue Variance from DRG Corrections ---
st.subheader("2. Revenue Variance from DRG Corrections")

variance_data = pd.DataFrame({
    "Category": ["Initial Coding Baseline", "Comorbidity/MCC Adjustments", "Physician Query Reassignments", "Final Audited Revenue"],
    "Estimated Revenue ($)": [1250000, 1342000, 1392500, 1392500],
    "Variance ($)": [0, 92000, 50500, 142500]
})

col_chart, col_table = st.columns([1, 1])

with col_chart:
    st.bar_chart(variance_data.set_index("Category")["Estimated Revenue ($)"])

with col_table:
    st.dataframe(variance_data, use_container_width=True)

st.divider()

# --- Section 3: DRG Denial and Rebill Tracking ---
st.subheader("3. DRG Denial & Rebill Tracking")

denials_data = pd.DataFrame({
    "Claim ID": ["CLM-8801", "CLM-8804", "CLM-8812", "CLM-8825", "CLM-8830"],
    "Patient ID": ["PT-10024", "PT-10088", "PT-10102", "PT-10145", "PT-10190"],
    "Initial DRG": ["DRG-282", "DRG-195", "DRG-638", "DRG-392", "DRG-282"],
    "Denial Reason": ["Clinical Documentation Gap", "Sequencing Error", "Lack of Medical Necessity", "Missing Secondary Code", "Clinical Documentation Gap"],
    "Rebill Status": ["Rebilled & Recovered", "Pending Appeal", "Rebilled & Recovered", "Under Review", "Rebilled & Recovered"],
    "Recovered Amount ($)": [6175.00, 0.00, 4800.00, 0.00, 6175.00]
})

st.dataframe(denials_data, use_container_width=True)
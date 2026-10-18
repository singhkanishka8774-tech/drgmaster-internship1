import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Documentation Query Workflow", layout="wide", page_icon="📝")

st.header("📝 Phase 3: Clinical Documentation Review & Physician Queries")
st.caption("Week 3: Identify Documentation Gaps, Route Queries, and Track Audit History")

# Initialize Session State for Audit History
if "query_audit_log" not in st.session_state:
    st.session_state.query_audit_log = []

# --- Section 1: Identify Documentation Gap ---
st.subheader("1. Identify Clinical Documentation Gap")

col1, col2 = st.columns(2)
with col1:
    patient_id = st.text_input("Patient ID", value="PT-10024")
    physician_name = st.text_input("Attending Physician", value="Dr. Smith")
with col2:
    suspected_condition = st.selectbox(
        "Suspected / Unconfirmed Condition", 
        ["Sepsis", "Acute Kidney Injury (AKI)", "Heart Failure Severity", "Malnutrition (Severe vs Moderate)", "Respiratory Failure"]
    )
    drg_impact = st.selectbox("Potential Impact", ["CC (Complication/Comorbidity)", "MCC (Major CC)", "DRG Reassignment"])

query_reason = st.text_area(
    "Clinical Indicator / Reason for Query", 
    placeholder="e.g., Lab results indicate elevated serum creatinine, but AKI is not explicitly documented in progress notes."
)

if st.button("📩 Send Query to Physician", type="primary"):
    if query_reason.strip() != "":
        new_entry = {
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Patient ID": patient_id,
            "Physician": physician_name,
            "Query Condition": suspected_condition,
            "Impact": drg_impact,
            "Status": "Pending Response",
            "Physician Response": "N/A"
        }
        st.session_state.query_audit_log.append(new_entry)
        st.success(f"Query successfully routed to {physician_name} for Patient {patient_id}!")
    else:
        st.warning("Please enter clinical indicators before routing the query.")

st.divider()

# --- Section 2: Audit History & Response Management ---
st.subheader("2. Query-Response Audit Trail")

if st.session_state.query_audit_log:
    audit_df = pd.DataFrame(st.session_state.query_audit_log)
    st.dataframe(audit_df, use_container_width=True)
    
    # Simulate Physician Clarification Response
    st.markdown("#### 🔄 Physician Response Simulator")
    selected_idx = st.selectbox("Select Query to Respond To", range(len(audit_df)), format_func=lambda x: f"Query {x+1}: {audit_df.iloc[x]['Patient ID']} - {audit_df.iloc[x]['Query Condition']}")
    
    physician_reply = st.radio("Physician Clarification", ["Confirmed (Update Coding)", "Ruled Out (No Change)", "More Info Needed"])
    response_notes = st.text_input("Physician Notes", value="Confirmed based on lab markers and clinical presentation.")
    
    if st.button("Update Audit Status"):
        st.session_state.query_audit_log[selected_idx]["Status"] = f"Resolved - {physician_reply}"
        st.session_state.query_audit_log[selected_idx]["Physician Response"] = response_notes
        st.success("Audit trail updated successfully!")
        st.rerun()
else:
    st.info("No queries generated yet. Submit a query above to begin the audit history.")
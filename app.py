import streamlit as st

st.set_page_config(
    page_title="DRGMaster Enterprise", 
    page_icon="🏥", 
    layout="wide"
)

st.title("🏥 DRGMaster: Enterprise DRG Mapping & Validation Engine")
st.markdown("### Inpatient Coding, Clinical Documentation, and Financial Analytics Platform")

st.info("👈 Select a module from the sidebar on the left to navigate through the project phases:")

st.markdown("""
* **Week 1: Single Patient Inpatient Intake** (`1_Single_Patient.py`) - Core DRG grouping, severity indexing, and reimbursement estimation.
* **Week 2: Batch Processing Engine** (`2_Batch_Processing.py`) - Bulk CSV/Excel validation, error tracking, and automated reporting.
* **Week 3: Documentation Query Workflow** (`3_Documentation_Query.py`) - Clinical gap identification, physician queries, and audit tracking.
* **Week 4: Financial & Quality Analytics** (`4_Financial_Analytics.py`) - Case-Mix Index (CMI) trends, revenue variance, and denial management.
""")
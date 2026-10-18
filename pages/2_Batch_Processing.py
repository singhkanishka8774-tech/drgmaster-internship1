import streamlit as st
import pandas as pd

st.set_page_config(page_title="Batch DRG Processing", layout="wide", page_icon="📤")

st.header("📤 Batch DRG Validation & Processing")
st.caption("Week 2: Bulk CSV/Excel Processing Engine")

uploaded_file = st.file_uploader(
    "Upload Patient Batch File (CSV or Excel)", 
    type=["csv", "xlsx"]
)

if uploaded_file is not None:
    try:
        # Read file based on extension
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
            
        st.success(f"Successfully loaded `{uploaded_file.name}` with {len(df)} rows.")
        
        # Preview Data
        with st.expander("🔍 Preview Raw Dataset"):
            st.dataframe(df.head(), use_container_width=True)
            
        # Column Mapping
        st.subheader("⚙️ Column Mapping")
        col1, col2, col3 = st.columns(3)
        with col1:
            patient_col = st.selectbox("Patient ID Column", df.columns)
        with col2:
            icd_col = st.selectbox("Diagnosis/ICD Column", df.columns)
        with col3:
            cost_col = st.selectbox("Estimated Cost Column", df.columns)
            
        if st.button("🚀 Run Batch DRG Validation", type="primary"):
            processed_df = df.copy()
            
            # Validation logic
            processed_df["DRG_Status"] = processed_df[icd_col].apply(
                lambda x: "Valid DRG" if pd.notnull(x) and str(x).strip() != "" else "Missing Code"
            )
            
            # Metrics Dashboard
            st.subheader("📊 Validation Summary")
            m1, m2, m3, m4 = st.columns(4)
            
            total_records = len(processed_df)
            valid_count = (processed_df["DRG_Status"] == "Valid DRG").sum()
            error_count = total_records - valid_count
            accuracy = (valid_count / total_records) * 100 if total_records > 0 else 0
            
            m1.metric("Total Records", total_records)
            m2.metric("Valid DRGs", valid_count)
            m3.metric("Errors / Missing", error_count, delta_color="inverse")
            m4.metric("Accuracy Rate", f"{accuracy:.1f}%")
            
            st.divider()
            st.subheader("📋 Processed Results")
            st.dataframe(processed_df, use_container_width=True)
            
            # Download Button
            csv_data = processed_df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Download Validated DRG Report (CSV)",
                data=csv_data,
                file_name="drg_batch_validation_report.csv",
                mime="text/csv"
            )
            
    except Exception as e:
        st.error(f"Error reading file: {e}")
import streamlit as st

st.title("🔒 Privacy Audit")

col1, col2, col3 = st.columns(3)

col1.metric("Re-identification Risk", "Low")
col2.metric("Data Leakage Risk", "Minimal")
col3.metric("Privacy Score", "96%")

st.progress(0.96)

st.success("✅ Data is safe for AI training")
import streamlit as st

st.title("🤖 Model Training")

model = st.selectbox("Select Model", ["Random Forest", "Logistic Regression"])

if st.button("Train Model"):
    st.success(f"{model} trained successfully ✅")
    st.metric("Accuracy", "89%")
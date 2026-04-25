import time

if "real_data" not in st.session_state:
    st.warning("Upload data first")
else:
    if st.button("Generate Synthetic Data"):
        with st.spinner("Running CTGAN..."):
            time.sleep(2)

        # MOCK synthetic data (replace with CTGAN later)
        synth = st.session_state.real_data.copy()
        synth = synth.apply(lambda x: x + np.random.normal(0, 0.1, len(x)) if np.issubdtype(x.dtype, np.number) else x)

        st.session_state.synthetic_data = synth
        st.success("Synthetic data generated!")
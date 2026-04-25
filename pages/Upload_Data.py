file = st.file_uploader("Upload CSV")

if file:
    df = pd.read_csv(file)
    st.session_state.real_data = df
    st.success("Real dataset loaded!")
    st.dataframe(df.head())
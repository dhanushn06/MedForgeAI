st.title("Compare Real vs Synthetic Data")

if "real_data" not in st.session_state or "synthetic_data" not in st.session_state:
    st.warning("Upload and generate data first")

else:
    real = st.session_state.real_data
    synth = st.session_state.synthetic_data

    numeric_cols = real.select_dtypes(include=np.number).columns

    if len(numeric_cols) == 0:
        st.error("No numeric columns found!")
    else:
        col = st.selectbox("Select Column", numeric_cols)

        # ── DISTRIBUTION COMPARISON ──
        st.subheader("Distribution Comparison")

        fig = go.Figure()
        fig.add_trace(go.Histogram(x=real[col], name="Real", opacity=0.6))
        fig.add_trace(go.Histogram(x=synth[col], name="Synthetic", opacity=0.6))

        fig.update_layout(barmode='overlay')
        st.plotly_chart(fig, use_container_width=True)

        # ── SIDE BY SIDE HEATMAPS ──
        st.subheader("Correlation Analysis")

        corr_real = real[numeric_cols].corr()
        corr_synth = synth[numeric_cols].corr()

        c1, c2 = st.columns(2)

        with c1:
            st.markdown("**Real Data**")
            fig1 = go.Figure(data=go.Heatmap(
                z=corr_real.values,
                x=corr_real.columns,
                y=corr_real.columns,
                colorscale='RdBu'
            ))
            st.plotly_chart(fig1, use_container_width=True)

        with c2:
            st.markdown("**Synthetic Data**")
            fig2 = go.Figure(data=go.Heatmap(
                z=corr_synth.values,
                x=corr_synth.columns,
                y=corr_synth.columns,
                colorscale='RdBu'
            ))
            st.plotly_chart(fig2, use_container_width=True)

        # ── 🔥 DIFFERENCE HEATMAP (THIS IS THE WOW PART) ──
        st.subheader("Correlation Difference (Real vs Synthetic)")

        diff = abs(corr_real - corr_synth)

        fig3 = go.Figure(data=go.Heatmap(
            z=diff.values,
            x=diff.columns,
            y=diff.columns,
            colorscale='Reds'
        ))
        st.plotly_chart(fig3, use_container_width=True)

        # ── 🔥 METRICS (VERY IMPORTANT FOR JUDGES) ──
        st.subheader("Statistical Similarity Score")

        score = 1 - diff.mean().mean()

        col1, col2, col3 = st.columns(3)

        col1.metric("Similarity Score", f"{score:.3f}")
        col2.metric("Avg Correlation Diff", f"{diff.mean().mean():.4f}")
        col3.metric("Columns Compared", len(numeric_cols))
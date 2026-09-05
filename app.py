import streamlit as st
import pandas as pd
import plotly.express as px

from evaluator.report import evaluate_dataset, export_report, summary_stats

st.set_page_config(page_title="LLM Evaluation Platform", page_icon="📊", layout="wide")

st.title("📊 LLM Evaluation Platform")
st.caption("Automated QA for prompt-response datasets | Built for AI/LLM Ops portfolios")

with st.sidebar:
    st.header("How to use")
    st.markdown(
        """
1. Upload a CSV with columns:
   - `prompt`
   - `response`
   - `expected`
   - `model_name` (optional)
2. Click **Run Evaluation**
3. Download the report
        """
    )
    st.divider()
    use_sample = st.toggle("Use sample dataset", value=True)

uploaded = st.file_uploader("Upload evaluation CSV", type=["csv"])

if use_sample and uploaded is None:
    df = pd.read_csv("data/sample.csv")
    st.info("Using bundled sample dataset from `data/sample.csv`.")
elif uploaded is not None:
    df = pd.read_csv(uploaded)
else:
    st.warning("Upload a CSV or enable the sample dataset.")
    st.stop()

st.subheader("Input Preview")
st.dataframe(df.head(10), use_container_width=True)

if st.button("Run Evaluation", type="primary"):
    with st.spinner("Running semantic, quality, and toxicity checks..."):
        results = evaluate_dataset(df)
        stats = summary_stats(results)

    st.success("Evaluation complete.")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Samples", stats["total_samples"])
    col2.metric("Pass Rate", f"{stats['pass_rate']}%")
    col3.metric("Avg Similarity", stats["avg_similarity"])
    col4.metric("Avg Overall", stats["avg_overall"])

    st.subheader("Results")
    st.dataframe(results, use_container_width=True)

    if "model_name" in results.columns:
        model_summary = (
            results.groupby("model_name")
            .agg(
                samples=("overall_score", "count"),
                pass_rate=("passed", "mean"),
                avg_similarity=("similarity_score", "mean"),
                avg_overall=("overall_score", "mean"),
            )
            .reset_index()
        )
        model_summary["pass_rate"] = (model_summary["pass_rate"] * 100).round(1)

        st.subheader("Model Comparison")
        st.dataframe(model_summary, use_container_width=True)

        fig = px.bar(
            model_summary,
            x="model_name",
            y="avg_overall",
            color="model_name",
            title="Average Overall Score by Model",
        )
        st.plotly_chart(fig, use_container_width=True)

    csv_report = export_report(results)
    st.download_button(
        label="Download Evaluation Report (CSV)",
        data=csv_report,
        file_name="llm_evaluation_report.csv",
        mime="text/csv",
    )

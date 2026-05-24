import streamlit as st
from scanner import run_full_scan
import pandas as pd

st.set_page_config(page_title="FULL MARKET SCANNER", layout="wide")

st.title("🌍 FULL MARKET SCANNER PRO")
st.markdown("Institutional Multi-Asset Scan Engine")

limit = st.slider("Scan Limit (for performance)", 100, 5000, 1000)
min_score = st.slider("Min Score", 0, 100, 70)

if st.button("🚀 START FULL SCAN"):

    with st.spinner("Scanning global market..."):
        results = run_full_scan(limit)

    df = pd.DataFrame(results)
    df = df[df["score"] >= min_score]

    st.success(f"{len(df)} setups found")

    st.dataframe(df)

    st.bar_chart(df.set_index("symbol")["score"])

    st.markdown("### 🔥 TOP 20 SETUPS")
    st.dataframe(df.head(20))

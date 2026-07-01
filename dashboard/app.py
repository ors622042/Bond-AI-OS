# Bond AI OS V4 Dashboard (Streamlit)

import streamlit as st
import pandas as pd
from indicators.score import etf_score
from config import ETFS

st.set_page_config(page_title="Bond AI OS Dashboard", layout="wide")

st.title("📊 Bond AI OS V4 Dashboard")
st.subheader("Daily Auto Investment Risk Monitor")

results = []

for etf in ETFS:
    results.append(etf_score(etf))

df = pd.DataFrame(results)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("00679B Score", df[df['etf']=='00679B']['score'].values[0])

with col2:
    st.metric("00740B Score", df[df['etf']=='00740B']['score'].values[0])

with col3:
    st.metric("00945B Score", df[df['etf']=='00945B']['score'].values[0])

st.divider()

st.dataframe(df)

st.divider()

st.bar_chart(df.set_index("etf")["score"])

st.caption("Auto-updated by Bond AI OS V4")

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import streamlit as st
import plotly.express as px
import pandas as pd
from app.theme import apply_theme

apply_theme()

st.title("Dataset Insights")
df=pd.read_csv("data/creditcard.csv")
fig=px.histogram(df, x="Amount", nbins=100, title="Transaction Amount Distribution")
st.plotly_chart(fig,width="stretch")
fig2=px.pie(df, names="Class", title="Fraud Distribution")
st.plotly_chart(fig2,width="stretch")

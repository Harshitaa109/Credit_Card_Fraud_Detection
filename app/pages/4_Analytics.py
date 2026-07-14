import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
import streamlit as st
import pandas as pd
import plotly.express as px
from app.theme import apply_theme

apply_theme()

st.set_page_config(page_title="Fraud Analytics", page_icon="📊", layout="wide")
st.title("Fraud Analytics Dashboard")
st.markdown("Explore the dataset through interactive visualizations and understand fraud patterns.")
@st.cache_data
def load_data(): return pd.read_csv("data/creditcard.csv")
df = load_data()
total, fraud = len(df), len(df[df["Class"] == 1])
normal, fraud_percent = len(df[df["Class"] == 0]), fraud / total * 100
avg_amount, highest = df["Amount"].mean(), df["Amount"].max()
c1,c2,c3,c4,c5 = st.columns(5)
c1.metric("Transactions", f"{total:,}"); c2.metric("Fraud Cases", fraud); c3.metric("Fraud %", f"{fraud_percent:.3f}%")
c4.metric("Average Amount", f"₹ {avg_amount:.2f}"); c5.metric("Highest Amount", f"₹ {highest:,.2f}")
st.divider()
left,right = st.columns(2)
pie = px.pie(df, names="Class", title="Fraud vs Legitimate", color="Class", color_discrete_map={0:"#2ECC71",1:"#E74C3C"})
pie.update_traces(textinfo="percent+label"); left.plotly_chart(pie, width="stretch")
hist = px.histogram(df, x="Amount", nbins=60, color="Class", title="Transaction Amount Distribution"); right.plotly_chart(hist, width="stretch")
st.divider()
time_fig = px.histogram(df, x="Time", color="Class", nbins=100, title="Transaction Time Distribution"); st.plotly_chart(time_fig, width="stretch")
st.divider()
box = px.box(df, x="Class", y="Amount", color="Class", title="Amount vs Fraud"); st.plotly_chart(box, width="stretch")
st.divider(); st.subheader("Correlation Heatmap")
heat = px.imshow(df.corr(numeric_only=True), aspect="auto", color_continuous_scale="RdBu_r"); st.plotly_chart(heat, width="stretch")
st.divider(); st.subheader("Fraud Transaction Statistics")
fraud_df = df[df["Class"] == 1]
stats = pd.DataFrame({"Metric":["Minimum Amount","Average Amount","Maximum Amount"],"Value":[fraud_df.Amount.min(),fraud_df.Amount.mean(),fraud_df.Amount.max()]})
st.dataframe(stats, width="stretch")

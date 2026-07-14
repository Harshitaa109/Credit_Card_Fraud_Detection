import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from src.config import METRICS_PATH
from app.theme import apply_theme

apply_theme()

st.set_page_config(page_title="Model Performance", page_icon="", layout="wide")
st.title("Machine Learning Model Performance")
st.markdown("Compare different Machine Learning models trained for Credit Card Fraud Detection.")
df = pd.read_csv(METRICS_PATH)
metrics_columns = ["Accuracy", "Precision", "Recall", "F1", "ROC_AUC"]
df[metrics_columns] = df[metrics_columns].round(4)
st.subheader("🥇 Model Leaderboard")
leader = df.sort_values(by="ROC_AUC", ascending=False).reset_index(drop=True); leader.index += 1
st.dataframe(leader, width="stretch")
best = leader.iloc[0]
st.success(f"Best Model: **{best['Model']}**\n\nROC-AUC Score: **{best['ROC_AUC']}**\n\nF1 Score: **{best['F1']}**")
st.divider(); st.subheader(" Performance Summary")
c1,c2,c3,c4 = st.columns(4)
c1.metric("Best Accuracy", f"{best['Accuracy']:.4f}"); c2.metric("Best Precision", f"{best['Precision']:.4f}")
c3.metric("Best Recall", f"{best['Recall']:.4f}"); c4.metric("Best F1", f"{best['F1']:.4f}")
st.divider(); st.subheader("Model Metrics Comparison")
melt = df.melt(id_vars="Model", value_vars=metrics_columns, var_name="Metric", value_name="Score")
fig = px.bar(melt, x="Metric", y="Score", color="Model", barmode="group", text_auto=".3f", title="Comparison of ML Models")
st.plotly_chart(fig, width="stretch")
st.divider(); st.subheader("🕸 Model Capability Radar")
radar = go.Figure()
for _, row in df.iterrows(): radar.add_trace(go.Scatterpolar(r=[row[m] for m in metrics_columns], theta=metrics_columns, fill="toself", name=row["Model"]))
radar.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0,1])), height=600)
st.plotly_chart(radar, width="stretch")
st.divider(); st.subheader("Performance Heatmap")
heat = px.imshow(df.set_index("Model")[metrics_columns], text_auto=".3f", aspect="auto", title="Metric Heatmap")
st.plotly_chart(heat, width="stretch")
st.divider(); st.subheader("🏅 Final Ranking")
for rank, (_, row) in enumerate(df.sort_values(by="ROC_AUC", ascending=False).iterrows(), start=1):
    st.metric(label=f"Rank {rank}", value=row["Model"], delta=f"ROC-AUC : {row['ROC_AUC']:.4f}")

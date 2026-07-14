import sys
from pathlib import Path
ROOT_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(ROOT_DIR))
import streamlit as st
import pandas as pd
import plotly.express as px
from src.config import FEATURE_IMPORTANCE_PATH, REPORT_DIR
from app.theme import apply_theme

apply_theme()

st.set_page_config(page_title="Explain AI", page_icon="", layout="wide")
st.title("Explainable AI - Fraud Detection")
st.markdown("This section explains how the fraud detection model makes decisions and which factors influence predictions.")
st.header("1. Global Feature Importance")
importance = pd.read_csv(FEATURE_IMPORTANCE_PATH).sort_values("Importance", ascending=True)
fig = px.bar(importance.tail(15), x="Importance", y="Feature", orientation="h", title="Top Features Influencing Fraud Detection")
st.plotly_chart(fig, width="stretch")
top_features = importance.sort_values("Importance", ascending=False).head(5)
st.subheader("Most Important Fraud Indicators")
for _, row in top_features.iterrows(): st.write(f"🔴 **{row['Feature']}**\n\nImportance Score: {row['Importance']:.3f}")
st.header("2. Fraud Pattern Analysis")
eda = pd.read_csv(REPORT_DIR / "eda_summary.csv")
col1,col2 = st.columns(2)
with col1:
    fig = px.bar(eda, x="Class", y="mean", title="Average Amount by Class", labels={"Class":"Transaction Type", "mean":"Average Amount"}); st.plotly_chart(fig, width="stretch")
with col2:
    fig = px.bar(eda, x="Class", y="count", title="Number of Transactions"); st.plotly_chart(fig, width="stretch")
fraud_data, normal_data = eda[eda["Class"]==1].iloc[0], eda[eda["Class"]==0].iloc[0]
st.subheader("Fraud Behaviour Insights")
st.info(f"Fraud transactions have an average amount of ₹{fraud_data['mean']:.2f}\n\nCompared to normal transactions: ₹{normal_data['mean']:.2f}\n\nFraud transactions show different feature patterns captured by the ML model.")
st.header("3. Model Performance & Confidence")
report = pd.read_csv(REPORT_DIR / "classification_report.csv")
fraud_row = report[report.iloc[:,0].astype(str)=="1"]
precision, recall, f1 = fraud_row["precision"].values[0], fraud_row["recall"].values[0], fraud_row["f1-score"].values[0]
col1,col2,col3=st.columns(3)
col1.metric("Fraud Precision", f"{precision*100:.2f}%"); col2.metric("Fraud Recall", f"{recall*100:.2f}%"); col3.metric("Fraud F1 Score", f"{f1*100:.2f}%")
st.header("4. AI Decision Summary")
st.success("The model identifies fraudulent transactions mainly through abnormal patterns in PCA-based features.\n\nMost influential features: V14, V10, V4, V12, V17.\n\nThe model achieves high fraud detection performance while maintaining very low false positives.")

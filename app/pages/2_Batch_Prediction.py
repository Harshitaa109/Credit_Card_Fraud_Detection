import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
import streamlit as st
import pandas as pd
from src.predict import FraudPredictor
from app.theme import apply_theme

apply_theme()

st.set_page_config(page_title="Fraud Prediction", page_icon="🤖")
st.title("🤖 Credit Card Fraud Prediction")
predictor = FraudPredictor()
uploaded = st.file_uploader("Upload csv file for prediction", type=["csv"])
if uploaded is not None:
    try:
        df = pd.read_csv(uploaded)
        st.success("Dataset uploaded successfully!")
        st.write("Dataset Shape")
        st.write(df.shape)
        result = predictor.predict(df)
        st.success("Prediction completed!")
        st.dataframe(result.head(30), width="stretch")
        st.dataframe(result.tail(30), width="stretch")
        output_path = "predictions.csv"
        result.to_csv(output_path, index=False)
        with open(output_path, "rb") as file:
            st.download_button(label=" Download Predictions", data=file, file_name="predictions.csv", mime="text/csv")
    except Exception as e:
        st.exception(e)

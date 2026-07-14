import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import streamlit as st
import pandas as pd
from app.theme import apply_theme

apply_theme()

st.title("Dataset Overview")
df = pd.read_csv("data/creditcard.csv")
st.write(df.head())
st.subheader("Dataset Shape")
st.write(df.shape)
st.subheader("Class Distribution")
st.bar_chart(df["Class"].value_counts())

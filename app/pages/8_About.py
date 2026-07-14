import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import streamlit as st
from app.theme import apply_theme

apply_theme()

st.title("About")
st.markdown("""
## Credit Card Fraud Detection

This project demonstrates an end-to-end Machine Learning pipeline.

### Tech Stack

- Python
- Scikit-learn
- Pandas
- Streamlit
- Joblib

### Developer

Harshitaa Sanwal

B.Tech Computer Science

Lovely Professional University
""")

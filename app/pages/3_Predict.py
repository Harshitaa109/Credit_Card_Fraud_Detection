import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT))
import streamlit as st
import pandas as pd
from src.predict import FraudPredictor
from app.theme import apply_theme

apply_theme()
st.set_page_config(page_title="Smart Fraud Simulator",page_icon="💳",layout="wide")
predictor=FraudPredictor()
@st.cache_data
def load_data(): return pd.read_csv("data/creditcard.csv")
df=load_data()
st.title("Smart Fraud Simulator")
st.write("Generate realistic credit card transactions and predict whether they are fraudulent using Machine Learning.")
st.divider()
scenario=st.selectbox("Select Transaction Scenario",["Grocery Shopping","Online Shopping","ATM Withdrawal","International Transaction","Suspicious Transaction","Random Transaction"])
col1,col2=st.columns(2)
amount=col1.number_input("Transaction Amount (₹)",min_value=0.0,value=1500.0,step=100.0)
hour=col2.slider("Transaction Hour",0,23,12)
if st.button("Generate Transaction"):
    if scenario=="⚠ Suspicious Transaction": transaction=df[df["Class"]==1].sample(1).copy()
    elif scenario=="Random Transaction": transaction=df.sample(1).copy()
    else: transaction=df[df["Class"]==0].sample(1).copy()
    transaction["Amount"]=pd.Series([float(amount)],index=transaction.index,dtype="float64")
    transaction["Time"]=pd.Series([float(hour*3600)],index=transaction.index,dtype="float64")
    transaction=transaction.drop(columns=["Class"])
    st.session_state["transaction"]=transaction
    st.success("Transaction Generated Successfully!")
if "transaction" in st.session_state:
    st.subheader("Generated Transaction")
    display_df=st.session_state["transaction"][["Time","Amount"]]
    col1,col2=st.columns(2)
    col1.metric("Amount",f"₹ {display_df.iloc[0]['Amount']:.2f}")
    col2.metric("Time",f"{hour}:00")
    with st.expander("Show Technical Features"): st.dataframe(st.session_state["transaction"])
st.divider()
if st.button("Predict Fraud"):
    if "transaction" not in st.session_state: st.warning("Generate a transaction first.")
    else:
        result=predictor.predict(st.session_state["transaction"])
        prediction=int(result["Prediction"].iloc[0]); probability=float(result["Fraud Probability"].iloc[0]); risk=result["Risk Level"].iloc[0]
        st.divider();st.subheader("Prediction Result")
        if prediction==1: st.error("Fraudulent Transaction");recommendation="Block Transaction Immediately"
        else: st.success("Legitimate Transaction");recommendation="Approve Transaction"
        c1,c2,c3=st.columns(3);c1.metric("Fraud Probability",f"{probability*100:.2f}%");c2.metric("Risk Level",risk);confidence=max(probability,1-probability)*100;c3.metric("Model Confidence",f"{confidence:.2f}%")
        st.progress(probability);st.subheader("Recommendation");st.info(recommendation);st.subheader("Prediction Output");st.dataframe(result)
        csv=result.to_csv(index=False);st.download_button("Download Prediction",csv,"prediction.csv","text/csv")

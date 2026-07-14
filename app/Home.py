import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import streamlit as st
import plotly.graph_objects as go
from app.theme import apply_theme

apply_theme()

st.set_page_config(page_title="Credit Card Fraud Detection", page_icon="💳", layout="wide", initial_sidebar_state="expanded")
st.markdown("""
<style>
.block-container{padding-top:2rem;padding-bottom:2rem;max-width:1200px;}
.hero{background:linear-gradient(135deg,#0F172A,#1E3A8A,#2563EB);padding:45px;border-radius:22px;color:white;box-shadow:0px 8px 30px rgba(0,0,0,.30);margin-bottom:35px;}
.metric-card{background:#161B22;padding:25px;border-radius:18px;text-align:center;border:1px solid #30363D;transition:0.3s;}
.metric-card:hover{transform:translateY(-6px);box-shadow:0px 8px 25px rgba(37,99,235,.35);}
.metric-value{font-size:38px;font-weight:bold;color:white;}.metric-label{font-size:17px;color:#B8BCC8;}
.feature-card{background:#161B22;padding:20px;border-radius:16px;border:1px solid #30363D;height:170px;}.feature-title{font-size:22px;font-weight:bold;margin-bottom:10px;}.feature-text{font-size:16px;color:#C9D1D9;}.footer{text-align:center;padding:30px;color:gray;}
</style>
""", unsafe_allow_html=True)
st.markdown("""<div class="hero"><h1>💳 Credit Card Fraud Detection AI</h1><h3>Detect fraudulent transactions using Machine Learning.</h3>This dashboard demonstrates an end-to-end Machine Learning pipeline capable of identifying fraudulent credit card transactions in real time.</div>""", unsafe_allow_html=True)
cards=[("284,807","Transactions"),("492","Fraud Cases"),("30","Features"),("99.97%","Best Accuracy")]
cols=st.columns(4)
for col,(value,label) in zip(cols,cards):
    with col: st.markdown(f'<div class="metric-card"><div class="metric-value">{value}</div><div class="metric-label">{label}</div></div>',unsafe_allow_html=True)
st.write("")
left,right=st.columns([1.1,1])
with left:
    st.subheader(" Fraud Distribution")
    fig=go.Figure(go.Pie(labels=["Legitimate","Fraud"],values=[284315,492],hole=.72,marker_colors=["#2563EB","#EF4444"]))
    fig.update_layout(template="plotly_dark",height=430,margin=dict(l=20,r=20,t=40,b=20)); st.plotly_chart(fig,width="stretch")
with right:
    st.subheader(" Model Accuracy")
    gauge=go.Figure(go.Indicator(mode="gauge+number",value=99.97,number={'suffix':'%'},gauge={'axis':{'range':[0,100]},'bar':{'color':'#10B981'},'steps':[{'range':[0,70],'color':'#7F1D1D'},{'range':[70,90],'color':'#B45309'},{'range':[90,100],'color':'#064E3B'}]}))
    gauge.update_layout(template="plotly_dark",height=430);st.plotly_chart(gauge,width="stretch")
st.markdown("---");st.subheader("⚙ Machine Learning Workflow")
c1,c2,c3,c4,c5=st.columns(5)
c1.success(" Dataset");c2.success(" Preprocessing");c3.success(" Train Models");c4.success(" Evaluate");c5.success(" Deploy")
st.markdown("---");st.subheader("Key Features")
col1,col2,col3=st.columns(3)
with col1: st.markdown('<div class="feature-card"><div class="feature-title"> Smart Prediction</div><div class="feature-text">• Real-time fraud prediction<br>• Probability score<br>• Risk categorization</div></div>',unsafe_allow_html=True)
with col2: st.markdown('<div class="feature-card"><div class="feature-title"> Analytics</div><div class="feature-text">• Model comparison<br>• ROC Curve<br>• Confusion Matrix<br>• Feature Importance</div></div>',unsafe_allow_html=True)
with col3: st.markdown('<div class="feature-card"><div class="feature-title"> Batch Prediction</div><div class="feature-text">• Upload CSV<br>• Download Results<br>• Fraud Detection Report</div></div>',unsafe_allow_html=True)
st.markdown("---");st.subheader(" Quick Actions")
a,b,c=st.columns(3)
with a: st.page_link("pages/3_Predict.py",label=" Start Prediction")
with b: st.page_link("pages/5_Model_Performance.py",label=" Model Performance")
with c: st.page_link("pages/7_Visualizations.py",label=" Visualizations")
st.markdown('<div class="footer">Made with ❤️ by <b>Harshitaa Sanwal</b><br><br>End-to-End Machine Learning Project | Streamlit | Scikit-Learn | Plotly</div>',unsafe_allow_html=True)

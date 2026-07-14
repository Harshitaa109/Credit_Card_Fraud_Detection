"""Shared dark amber styling for the Streamlit app."""

import streamlit as st


def apply_theme() -> None:
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Manrope:wght@400;500;600;700;800&display=swap');

        :root { --amber:#f5a524; --amber-soft:#ffd27a; --ink:#0b0d10; --surface:#15191f;
                --surface-2:#1b2028; --line:#303845; --text:#f6f1e7; --muted:#aab2bf; }
        html, body, [class*="css"] { font-family:Manrope, Arial, sans-serif; }
        .stApp { background:radial-gradient(circle at 78% -15%, #362309 0, transparent 27%), #0b0d10; }
        .block-container { max-width:1280px; padding-top:2.2rem; padding-bottom:3rem; }
        [data-testid="stSidebar"] { background:linear-gradient(180deg,#101318,#0b0d10); border-right:1px solid #2b3039; }
        [data-testid="stSidebarNav"] a { border-radius:9px; margin:3px 8px; transition:all .2s ease; }
        [data-testid="stSidebarNav"] a:hover { background:rgba(245,165,36,.13); color:var(--amber) !important; transform:translateX(3px); }
        h1, h2, h3 { letter-spacing:-.035em; }
        h1 { font-weight:800 !important; }
        [data-testid="stMetric"] { background:linear-gradient(145deg,#191e25,#12161b); border:1px solid var(--line);
          border-radius:14px; padding:1.1rem; transition:transform .22s ease, box-shadow .22s ease, border-color .22s ease; }
        [data-testid="stMetric"]:hover { transform:translateY(-4px); border-color:rgba(245,165,36,.75); box-shadow:0 13px 30px rgba(0,0,0,.32); }
        [data-testid="stMetricLabel"] { color:var(--muted); font-size:.78rem; font-weight:700; text-transform:uppercase; letter-spacing:.06em; }
        [data-testid="stMetricValue"] { color:var(--amber-soft); font-family:'DM Mono',monospace; }
        .stButton > button, [data-testid="stPageLink"] a { border-radius:9px; font-weight:700; border:1px solid rgba(245,165,36,.5);
          transition:transform .2s ease, background .2s ease, box-shadow .2s ease; }
        .stButton > button:hover, [data-testid="stPageLink"] a:hover { transform:translateY(-2px); background:#f5a524; color:#111 !important; box-shadow:0 10px 24px rgba(245,165,36,.22); }
        .stButton > button[kind="primary"] { background:linear-gradient(135deg,#f5a524,#e88a13); color:#15100a; border:none; }
        [data-testid="stFileUploader"] { background:linear-gradient(145deg,#181d24,#12161b); border:1.5px dashed #8b641e;
          border-radius:14px; padding:1rem; transition:all .25s ease; }
        [data-testid="stFileUploader"]:hover { border-color:var(--amber); background:rgba(245,165,36,.07); box-shadow:inset 0 0 0 1px rgba(245,165,36,.2); }
        [data-testid="stFileUploaderDropzone"] { border:0 !important; background:transparent !important; }
        [data-testid="stFileUploaderDropzone"] button { border-radius:7px; background:#2b210f; color:var(--amber-soft); border-color:#8b641e; }
        [data-testid="stTextInput"] input, [data-testid="stNumberInput"] input, [data-baseweb="select"] > div { background:#15191f !important; border-color:#3b4452 !important; border-radius:8px !important; }
        [data-testid="stTextInput"] input:focus, [data-testid="stNumberInput"] input:focus { border-color:var(--amber) !important; box-shadow:0 0 0 2px rgba(245,165,36,.18) !important; }
        [data-testid="stSlider"] [data-baseweb="slider"] div[role="slider"] { background:var(--amber) !important; }
        [data-testid="stDataFrame"] { border:1px solid var(--line); border-radius:10px; overflow:hidden; }
        [data-testid="stExpander"] { border:1px solid var(--line); border-radius:10px; background:#15191f; }
        [data-testid="stAlert"] { border-radius:10px; }
        hr { border-color:#2b3039; }
        .hero { position:relative; overflow:hidden; }
        .hero:after { content:""; position:absolute; width:280px; height:280px; background:radial-gradient(circle,rgba(245,165,36,.25),transparent 68%); right:-80px; top:-120px; pointer-events:none; }
        @keyframes amber-entry { from { opacity:0; transform:translateY(10px); } to { opacity:1; transform:translateY(0); } }
        [data-testid="stVerticalBlock"] > div { animation:amber-entry .35s ease both; }
        @media (prefers-reduced-motion:reduce) { *, *::before, *::after { animation:none !important; transition:none !important; } }
        </style>
        """,
        unsafe_allow_html=True,
    )

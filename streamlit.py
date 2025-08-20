import streamlit as st
import pandas as pd
import sqlite3
from io import StringIO

# Page configuration
st.set_page_config(
    page_title="Huda Beauty SQL Escape Room",
    page_icon="💄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #ff4b4b;
        text-align: center;
    }
    .challenge-box {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .success-box {
        background-color: #d4edda;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .code-box {
        background-color: #2d3b45;
        color: white;
        padding: 15px;
        border-radius: 10px;
        font-family: monospace;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# App title and description
st.markdown('<h1 class="main-header">💄 Huda Beauty SQL Escape Room</h1>', unsafe_allow_html=True)
st.markdown("""
Welcome to the Huda Beauty Growth Readiness Challenge! As a data analyst at Huda Beauty, 
your mission is to unlock the Growth Readiness Dossier by solving 5 SQL puzzles. 
Each lock requires you to write SQL queries to analyze our customer, product, and sales data.
""")

# Initialize session state for game progress
if 'current_lock' not in st.session_state:
    st.session_state.current_lock = 0
if 'locks_unlocked' not in st.session_state:
    st.session_state.locks_unlocked = [False] * 6
if 'sql_connection' not in st.session_state:
    st.session_state.sql_connection = None
if 'datasets' not in st.session_state:
    st.session_state.datasets = {}

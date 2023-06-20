import streamlit as st
from backend import backend

def frontend():
    st.write(backend("Hello", "World"))
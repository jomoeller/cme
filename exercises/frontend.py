import streamlit as st
import plotly.express as px
import pandas as pd
from backend import backend

def frontend():

    params = ["hello", "world"] 
    kwargs = {"hello": "world"}
    results = backend(*params, **kwargs)
    st.write(results)
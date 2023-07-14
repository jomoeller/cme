import streamlit as st
#import plotly.express as px
import pandas as pd
from backend import backend

def frontend():
    chemical_composition = {'c(Fe) (%)': 91, 'c(C) (%)':1, 'c(N) (%)':1, 'c(Cr) (%)':1, 'c(Ni) (%)':1,
       'c(Mo) (%)':1, 'c(Al) (%)':1, 'c(Mn) (%)':1, 'c(Cu) (%)':1, 'c(Si) (%)':1}
    results = backend(**chemical_composition)
    st.write(results)

    rows = [st.columns(5), st.columns(5)]
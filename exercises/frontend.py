import streamlit as st
import plotly.express as px
import pandas as pd
from backend import backend, elements

def frontend():

    with st.form("input"):
        rows = [st.columns(5), st.columns(5)]
        disabled = [True if "Fe" in el else False for el in elements]
        for e, element in enumerate(elements):
            r = int(e/5)
            i = e%5
            if "Fe" not in element:
                rows[r][i].number_input(element, key=element)
            else:
                rows[r][i].text_input(element, value="Rest", key=element, disabled=True)
        submitted = st.form_submit_button("Calculate properties")
    
    if submitted:
        chemical_composition = {el: st.session_state[el] for el in elements}
        chemical_composition["c(Fe) (%)"] = 100 - sum([st.session_state[el] for el in elements if "Fe" not in el])
        if chemical_composition["c(Fe) (%)"] < 0:
            st.error("Sum of all element contents must not be more than 100%.")
            st.stop()

        results = backend(**chemical_composition)
        st.success(f"For this composition an ultimate tensile strength of {int(results['Rm (MPa)'])} MPa and a fracture strain of {round(results['A (%)'],1)} % is predicted.")
        
        st.write("**Comparison to training data**")
        data = [*chemical_composition.values(), results["Rm (MPa)"], results["A (%)"], "Prediction"]
        columns = [*chemical_composition.keys(), "Rm (MPa)", "A (%)", "Type of Steel"]
        _df = pd.DataFrame([data], columns=columns)
        df = pd.concat([results["df"], _df])
        df["Size"] = 5
        df.iloc[-1,-1] = 20
        fig = px.scatter(df, x="Rm (MPa)", y="A (%)", color="Type of Steel", 
                         size="Size", hover_data=[c for c in df.columns if "c(" in c])
        st.plotly_chart(fig)
        
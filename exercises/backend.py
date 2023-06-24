import pickle
import os
import pandas as pd

elements = ['c(Fe) (%)', 'c(C) (%)', 'c(N) (%)', 'c(Cr) (%)', 'c(Ni) (%)',
            'c(Mo) (%)', 'c(Al) (%)', 'c(Mn) (%)', 'c(Cu) (%)', 'c(Si) (%)']

folder = os.path.dirname(os.path.abspath(__file__))

scaler = pickle.load(open(folder+os.sep+"scaler.pickle", "rb"))
model_A = pickle.load(open(folder+os.sep+"model_A.pickle", "rb"))
model_Rm = pickle.load(open(folder+os.sep+"model_Rm.pickle", "rb"))

df = pd.read_csv(folder+os.sep+"steel-data.csv", index_col=0)
df = df.dropna(subset=[*df.columns[6:16], "Rm (MPa)", "A (%)"])

def backend(*params, **kwargs): 
    x_unscaled = [kwargs[el] for el in elements]
    x = scaler.transform([x_unscaled])

    results = {
        "A (%)": model_A.predict(x)[0],
        "Rm (MPa)": model_Rm.predict(x)[0],
        "composition (scaled)": x,
        "composition (%)": x_unscaled, 
        "df": df
    }
    return results
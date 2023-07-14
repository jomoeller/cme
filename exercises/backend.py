import pickle
import os
import pandas as pd

# The path to the folder where this file is located, i.e. the cme/exercises folder: 
folder = os.path.dirname(os.path.abspath(__file__))

scaler = pickle.load(open(folder+os.sep+"scaler.pickle", "rb"))
model_A = pickle.load(open(folder+os.sep+"model_A.pickle", "rb"))
model_Rm = pickle.load(open(folder+os.sep+"model_Rm.pickle", "rb"))

def backend(*params, **kwargs): 
    
    x_unscaled = list(kwargs.values())
    x = scaler.transform([x_unscaled])

    pA = model_A.predict(x)[0]
    pRm = model_Rm.predict(x)[0]

    return {"A (%)": pA, "Rm (MPa)": pRm}
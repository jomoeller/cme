import pickle
import os
import pandas as pd

# The path to the folder where this file is located, i.e. the cme/exercises folder: 
folder = os.path.dirname(os.path.abspath(__file__))

def backend(*params, **kwargs): 
    
    return params, kwargs
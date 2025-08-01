import src.Configuration
import pandas as pd 
import numpy as np 
def ReadExcelFile(filename,headerrow):
    return pd.read_excel(filename,header=headerrow);
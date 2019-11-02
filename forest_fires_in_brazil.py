import pandas as pd
import numpy as np

file = "c:/Users/Czimer Máté/Documents/PythonScripts/csvs/amazon.csv"

# Create DataFrame object
df = pd.read_csv(file, encoding="latin1")
# print(df.head(),'\n', df.tail())

no_per_year = df.groupby()["year"].sum("number")
print(no_per_year)

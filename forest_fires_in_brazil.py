import pandas as pd
import numpy as np

file = "c:/git/HomeProject/csvs/amazon.csv"

# Create DataFrame object
df = pd.read_csv(file, encoding="latin1")
# print(df.head(),'\n', df.tail())

# Create some plots to visualize the dataset
df.plot(kind="scatter", x="year", y="number")

print(df.head())

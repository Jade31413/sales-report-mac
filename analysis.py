import pandas as pd

df = pd.read_csv("sales.csv")
print("rows:", len(df))
print("mean sale:", df["amount"].mean())
print("largest sale:", df["amount"].max())
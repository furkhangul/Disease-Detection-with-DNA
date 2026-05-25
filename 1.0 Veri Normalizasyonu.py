import pandas as pd
from sklearn.preprocessing import MinMaxScaler

veri = pd.read_csv("gene_expression.csv")

scaler = MinMaxScaler()

normalize_sutunlar = ["Gen1", "Gen2"]

veri[normalize_sutunlar] = scaler.fit_transform(veri[normalize_sutunlar])

veri.to_csv("Normalize_Veri.csv", index=False)


normalize = pd.read_csv("Normalize_Veri.csv")
print(normalize.to_string())

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

veri = pd.read_csv("Encoding_Veri.csv")

scaler = MinMaxScaler()

sayisal_sutunlar = ["Yas", "VKI"]

veri[sayisal_sutunlar] = scaler.fit_transform(veri[sayisal_sutunlar])

veri.to_csv("Normalize_Veri.csv", index=False)


normalize = pd.read_csv("Normalize_Veri.csv")
print(normalize.to_string())

import pandas as pd

veri = pd.read_csv("Normalize_Veri.csv")

deger = veri["Kanser"].value_counts()
oran = deger.max() / deger.min()

print(oran)

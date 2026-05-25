import pandas as pd
from sklearn import preprocessing

veri = pd.read_csv("yeniVeri.csv")
veri = veri.drop(["Ad", "Soyad"], axis=1)

# LabelEncoding
le = preprocessing.LabelEncoder()
label_sutunlar = [
    "APOE_e4_Geni", "APC_Geni_Mutasyonu", "CFTR_Geni_Mutasyonu",
    "T2_Diyabet", "Alzheimer", "Kolorektal_Kanser", "Kistik_Fibrozis"
]
for sutun in label_sutunlar:
    veri[sutun] = le.fit_transform(veri[sutun])

# OneHotEncoding
onehot_sutunlar = [
    "Cinsiyet", "Sigara_Durumu", "Alkol_Tuketimi",
    "Egzersiz_Seviyesi", "Aile_Gecmisi", "T2_Diyabet_Risk_Geni"
]
veri = pd.get_dummies(veri, columns=onehot_sutunlar, dtype=int)

print(veri.to_string())
veri.to_csv("Encoding_Veri.csv", index=False)

import pandas as pd
from imblearn.over_sampling import SMOTE

df = pd.read_csv("Normalize_Veri.csv")

hedefler = [
    "T2_Diyabet",
    "Alzheimer",
    "Kolorektal_Kanser",
    "Kistik_Fibrozis"
]

X = df.drop(columns=hedefler)

sonuc = X.copy()

for hedef in hedefler:

    y = df[hedef]

    smote = SMOTE(random_state=42)

    X_res, y_res = smote.fit_resample(X, y)

    sonuc[hedef] = y_res

sonuc.to_csv("Dengeli_Veri.csv", index=False)

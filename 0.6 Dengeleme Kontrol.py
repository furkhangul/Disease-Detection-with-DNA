import pandas as pd


veri = pd.read_csv("Dengeli_Veri.csv")

hastaliklar = [ "T2_Diyabet", "Alzheimer", "Kolorektal_Kanser", "Kistik_Fibrozis" ]

for hastalik in hastaliklar:
    degerler = veri[hastalik].value_counts()
    oran = degerler.max() / degerler.min()

    print(hastalik, oran)

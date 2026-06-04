import pandas as pd

veri = pd.read_csv('Veriler.csv', na_values=['', ' ', '#N/A', 'N/A', 'NULL'])

#Sayısal veriler için:
yas_ortalama = veri['Yas'].mean()
veri['Yas'] = veri['Yas'].fillna(round(yas_ortalama))

vki_ortalama = veri['VKI'].mean()
veri['VKI'] = veri['VKI'].fillna(round(vki_ortalama, 1))

#Kategorik veriler için:
veri['Cinsiyet'] = veri['Cinsiyet'].fillna(veri['Cinsiyet'].mode()[0])
veri['Sigara_Durumu'] = veri['Sigara_Durumu'].fillna(veri['Sigara_Durumu'].mode()[0])
veri['Alkol_Tuketimi'] = veri['Alkol_Tuketimi'].fillna(veri['Alkol_Tuketimi'].mode()[0])
veri['Egzersiz_Seviyesi'] = veri['Egzersiz_Seviyesi'].fillna(veri['Egzersiz_Seviyesi'].mode()[0])

#Sabit veriler için:
veri['Aile_Gecmisi'] = veri['Aile_Gecmisi'].fillna('Bilinmiyor')
veri.to_csv('yeniVeri.csv',index=False)


yeniVeri = pd.read_csv('yeniVeri.csv')
print(yeniVeri.to_string())

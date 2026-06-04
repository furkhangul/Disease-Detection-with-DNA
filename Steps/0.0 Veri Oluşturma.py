import csv
import random

# Veri havuzları
adlar_erkek = ["Furkan","Fırat","Samet","Ümit","Ahmet", "Mehmet", "Ali", "Mustafa", "Hasan", "Ibrahim", "Osman", "Halil", "Kemal", "Yusuf", "Burak",
               "Omer", "Serkan", "Gokhan", "Fatih"]
adlar_kadin = ["Ayse", "Fatma", "Zeynep", "Elif", "Hatice", "Merve", "Emine", "Gulay", "Hulya", "Sevgi", "Esra",
               "Tugba", "Aylin", "Derya", "Ceren"]
soyadlar = ["Yilmaz", "Demir", "Kaya", "Celik", "Sahin", "Ozturk", "Yildiz", "Aydin", "Ozdemir", "Arslan", "Dogan",
            "Kilic", "Tekin", "Turan", "Koc"]
sigara = ["Kullanmiyor", "Kullanıyor", "Bırakmis"]
alkol = ["Hic", "Haftada 1-2", "Haftada 3-4", "Her Gun"]
egzersiz = ["Dusuk", "Orta", "Yuksek"]
aile_gecmisi = ["Var", "Yok",   ]


def eksik_veri_yap(deger, ihtimal=0.08):
    """Belirli bir ihtimalle veriyi eksik (None) yapar."""
    return "" if random.random() < ihtimal else deger


veriler = []
# Sütun Başlıkları
basliklar = ["Ad", "Soyad", "Cinsiyet", "Yas", "VKI", "Sigara_Durumu", "Alkol_Tuketimi",
             "Egzersiz_Seviyesi", "Aile_Gecmisi", "T2_Diyabet_Risk_Geni", "APOE_e4_Geni",
             "APC_Geni_Mutasyonu", "CFTR_Geni_Mutasyonu", "T2_Diyabet", "Alzheimer",
             "Kolorektal_Kanser", "Kistik_Fibrozis"]
veriler.append(basliklar)

for _ in range(1000):
    # Temel Demografi
    cinsiyet = random.choice(["Erkek", "Kadin"])
    ad = random.choice(adlar_erkek) if cinsiyet == "Erkek" else random.choice(adlar_kadin)
    soyad = random.choice(soyadlar)
    yas = random.randint(20, 85)
    vki = round(random.uniform(18.5, 38.0), 1)

    # Yasam Tarzi
    s_durum = random.choice(sigara)
    a_durum = random.choice(alkol)
    e_durum = random.choice(egzersiz)
    a_gecmis = random.choice(aile_gecmisi)

    # Genetik Belirteçler (Doğal dengesizlikler ile)
    t2_gen = random.choices(["Dusuk", "Orta", "Yuksek"], weights=[50, 30, 20])[0]
    apoe_gen = random.choices(["Negatif", "Pozitif"], weights=[80, 20])[0]
    apc_gen = random.choices(["Negatif", "Pozitif"], weights=[90, 10])[0]
    cftr_gen = random.choices(["Negatif", "Pozitif"], weights=[95, 5])[0]

    # Hastalik Mantiklari (Veri madenciliginde algoritmalarin bulmasi gereken kaliplar)
    t2_hastalik = "Var" if (t2_gen == "Yuksek" and vki > 28) or (yas > 60 and s_durum == "Kullanıyor") else "Yok"
    alz_hastalik = "Var" if (apoe_gen == "Pozitif" and yas > 65) else "Yok"
    kol_hastalik = "Var" if (
                apc_gen == "Pozitif" or (a_gecmis == "Var" and s_durum == "Kullanıyor" and yas > 50)) else "Yok"
    cf_hastalik = "Var" if cftr_gen == "Pozitif" else "Yok"

    # Verileri formatlama ve rastgele eksik veri (NaN) ekleme
    satir = [
        ad,
        soyad,
        eksik_veri_yap(cinsiyet, 0.05),
        eksik_veri_yap(yas, 0.06),
        eksik_veri_yap(vki, 0.07),
        eksik_veri_yap(s_durum, 0.05),
        eksik_veri_yap(a_durum, 0.08),
        eksik_veri_yap(e_durum, 0.05),
        eksik_veri_yap(a_gecmis, 0.04),
        t2_gen, apoe_gen, apc_gen, cftr_gen,  # Gen verileri laboratuvardan geldiginden eksik olmaz
        t2_hastalik, alz_hastalik, kol_hastalik, cf_hastalik
    ]
    veriler.append(satir)

# CSV'ye yazdirma
with open('Veriler.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(veriler)

print("kalitsal_hastaliklar_1000.csv basariyla olusturuldu!")

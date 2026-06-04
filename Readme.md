# 🧬 Gen İfade Verisiyle Kanser Riski Tespiti

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.x-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)



</div>

---

## 📌 Proje Özeti

Bu proje, **gen ifadesi (gene expression)** verilerini kullanarak bireylerin kanser riskini tahmin eden makine öğrenmesi modelleri geliştirmeyi amaçlamaktadır. İki sayısal özellik (`Gen1`, `Gen2`) üzerinde dört farklı algoritma uygulanmış; bias-varyans dengesi, K-Fold doğrulama ve dengesiz sınıf problemi detaylı biçimde incelenmiştir.

---

## ✨ Özellikler

| # | Başlık | Açıklama |
|---|--------|----------|
| 1 | 🔍 **EDA** | Sınıf dağılımı, dağılım grafikleri, korelasyon matrisi |
| 2 | ⚙️ **Ön İşleme** | StandardScaler normalizasyonu, stratified train/test split |
| 3 | 📉 **Bias-Varyans** | Karar ağacı derinliğine göre eğitim/test hata analizi |
| 4 | 🔁 **K-Fold CV** | K=5 ve K=10 cross validation karşılaştırması |
| 5 | 🤖 **4 Algoritma** | KNN, Karar Ağacı, Naive Bayes, K-Means |
| 6 | 📊 **Değerlendirme** | Confusion Matrix, ROC-AUC, F1-Score, Jaccard İndeksi |
| 7 | ⚖️ **Dengesiz Sınıf** | SMOTE ve class_weight ile imbalanced data analizi |

---

## 🗂️ Repo Yapısı

```
kanser-riski-ml/
│
├── 📓 Furkan_Gul_2311505269_Kanser_Riski.ipynb   # Ana notebook
├── 📄 gene_expression.csv                         # Veri seti
├── 📝 README.md                                   # Bu dosya
└── 📑 Kanser_Riski_Rapor.docx                    # Proje raporu
```

---

## 🤖 Kullanılan Algoritmalar

```
┌─────────────────┬──────────────────┬──────────────────────────────────────────┐
│ Model           │ Tür              │ Temel Fikir                              │
├─────────────────┼──────────────────┼──────────────────────────────────────────┤
│ KNN (k=5)       │ Mesafeye dayalı  │ En yakın K komşunun çoğunluk sınıfı     │
│ Karar Ağacı     │ Kural tabanlı    │ If-else ağacı (max_depth=5)              │
│ Naive Bayes     │ Olasılıksal      │ Bayes teoremi + bağımsızlık varsayımı   │
│ K-Means         │ Kümeleme         │ Gözetimsiz, doğal küme tespiti          │
└─────────────────┴──────────────────┴──────────────────────────────────────────┘
```

---

## 📊 Veri Seti

| Özellik | Değer |
|---------|-------|
| **Kaynak** | `gene_expression.csv` |
| **Giriş değişkenleri** | `Gen1`, `Gen2` (sayısal) |
| **Hedef değişken** | `Kanser` — `0` Sağlıklı / `1` Kanser |
| **Sınıf dengesi** | %50 Sağlıklı — %50 Kanser |
| **Eksik değer** | Yok ✅ |

---

## 🚀 Kurulum ve Çalıştırma

### 1. Repoyu klonla

```bash
git clone https://github.com/furkhangul/Disease-Detection-with-DNA.git
cd Disease-Detection-with-DNA
```

### 2. Gerekli kütüphaneleri yükle

```bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
```

### 3. Notebook'u çalıştır

```bash
jupyter notebook Kanser_Risk_Analizi.ipynb
```

---

## 📦 Gereksinimler

```
pandas
numpy
matplotlib
seaborn
scikit-learn
scipy
jupyter
```

---

## 📈 Değerlendirme Metrikleri

| Metrik | Açıklama |
|--------|----------|
| **Accuracy** | Genel doğruluk oranı |
| **Precision** | Kanser dediğinde ne kadar doğru? |
| **Recall** | Kanserlerin kaçını yakaladık? |
| **F1-Score** | Precision & Recall harmonik ortalaması |
| **Jaccard** | Küme örtüşme benzerliği (0–1 arası) |
| **AUC-ROC** | Eşik bağımsız sınıflandırma başarısı |

> ⚠️ **Not:** Dengesiz sınıflarda Accuracy yanıltıcı olabilir. F1-Score ve AUC daha güvenilir metriklerdir.

---

## 🧪 Temel Bulgular

- **Bias-Varyans:** Karar ağacında derin yapılar overfitting'e yol açmaktadır.
- **K-Fold:** K=5 ve K=10 sonuçları birbirine yakın; model kararlı.
- **Dengesiz Sınıf:** Yapay dengesizlik senaryosunda Accuracy yüksek kalırken F1-Score belirgin düşmüştür.
- **En İyi Model:** En yüksek AUC değerine sahip model en iyi sınıflandırıcı olarak değerlendirilmiştir.

---

## 📚 Kaynakça

1. Géron, A. (2019). *Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow*. O'Reilly Media.
2. [Scikit-learn Documentation](https://scikit-learn.org/stable/)
3. Hastie, T., Tibshirani, R., & Friedman, J. (2009). *The Elements of Statistical Learning*. Springer.
4. He, H., & Garcia, E. A. (2009). Learning from Imbalanced Data. *IEEE TKDE*.

---

<div align="center">

**Furkan Gül · 2311505269 · Veri Madenciliği 2025-2026 Bahar**

</div>

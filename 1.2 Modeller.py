import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.cluster import KMeans

veri = pd.read_csv("Normalize_Veri.csv")

X = veri[["Gen1", "Gen2"]].values
y = veri["Kanser"].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# KNN ile çözüm
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
knn_tahmin = knn.predict(X_test)


# Karar Ağacı ile çözüm
karar_agaci = DecisionTreeClassifier(max_depth=5, random_state=42)
karar_agaci.fit(X_train, y_train)
karar_agaci_tahmin = karar_agaci.predict(X_test)


# Naive Bayes ile çözüm
naive_bayes = GaussianNB()
naive_bayes.fit(X_train, y_train)
naive_bayes_tahmin = naive_bayes.predict(X_test)


# K-Means ile çözüm
kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)
kmeans.fit(X)
kmeans_tahmin = kmeans.labels_

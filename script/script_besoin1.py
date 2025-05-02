import joblib
import numpy as np
import sys

# Charger le modèle KMeans et le scaler enregistrés
kmeans = joblib.load('C:/Users/SURFACE/Documents/ISEN/CIPA4/Projet Big Data_IA_Web/Projet Big Data_IA_Web/Web/Web/script/modele_kmeans.pkl')
scaler = joblib.load('C:/Users/SURFACE/Documents/ISEN/CIPA4/Projet Big Data_IA_Web/Projet Big Data_IA_Web/Web/Web/script/scaler.pkl')

hauteur = float(sys.argv[1])
diametre = float(sys.argv[2])

data = np.array([[hauteur, diametre]])
data_scaled = scaler.transform(data)

# Prédiction du cluster
cluster = kmeans.predict(data_scaled)
print(cluster[0])


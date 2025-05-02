from flask import Flask, request, jsonify
import joblib
import pandas as pd
from flask_cors import CORS
app = Flask(__name__)
CORS(app, resources={r"/estimer_age": {"origins": "*"}})





# Chargement du modèle
try:
    model = joblib.load("modele_trained.pkl")
    print("✅ Modèle chargé avec succès.")
except Exception as e:
    print("❌ Erreur de chargement :", e)
    model = None

@app.route('/estimer_age', methods=['POST'])
@app.route('/estimer_age', methods=['POST'])
def estimer_age():
    if not model:
        print("❌ Modèle non chargé.")
        return jsonify({'error': 'Modèle non chargé'}), 500

    try:
        data = request.get_json()
        print("[DEBUG] Données reçues :", data)

        espece = data.get("espece")
        hauteur_totale = float(data.get("hauteur_totale"))
        hauteur_tronc = float(data.get("hauteur_tronc"))
        diametre_tronc = float(data.get("diametre_tronc"))

        # Construction du DataFrame avec noms de colonnes exacts attendus par le pipeline
        X = pd.DataFrame([{
            "nomfrancais": espece,
            "haut_tot": hauteur_totale,
            "haut_tronc": hauteur_tronc,
            "tronc_diam": diametre_tronc
        }])

        print("[DEBUG] DataFrame pour prédiction :\n", X)

        prediction = model.predict(X)
        age_estime = round(float(prediction[0]), 1)
        print("[DEBUG] Âge prédit :", age_estime)

        return jsonify({'age': age_estime})

    except Exception as e:
        import traceback
        print("❌ Exception attrapée dans /estimer_age :")
        traceback.print_exc()  # Affiche l’erreur complète dans le terminal
        return jsonify({'error': 'Erreur serveur'}), 500


if __name__ == '__main__':
    app.run(debug=True)

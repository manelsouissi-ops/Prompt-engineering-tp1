
import requests

# Adresse de l'API HTTP locale d'Ollama
API_URL = "http://localhost:11434/api/chat"

# Données de la requête
payload = {
    "model": "qwen3:1.7b",
    "messages": [
        {
            "role": "user",
            "content": "Explique le machine learning en deux phrases."
        }
    ],
    "stream": False,
    "think": False
}

# Envoyer la requête HTTP POST
response = requests.post(API_URL, json=payload, timeout=180)

# Vérifier l'absence d'erreur HTTP
response.raise_for_status()

# Convertir le JSON reçu en dictionnaire Python
data = response.json()

# Afficher les résultats
print("Réponse :", data["message"]["content"])
print("Code HTTP :", response.status_code)

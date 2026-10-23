
from ollama import chat

MODEL = "gemma3:4b"

# Le SDK prépare la requête et convertit la réponse
response = chat(
    model=MODEL,
    messages=[
        {
            "role": "user",
            "content": "Explique le deep learning en deux phrases."
        }
    ],
    think=False,
    stream=False
)

print("Réponse :", response.message.content)
print("Modèle :", response.model)

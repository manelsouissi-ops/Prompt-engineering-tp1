
from ollama import chat

MODEL = "gemma3:4b"

SYSTEM_PROMPT = (
    "Tu es un chercheur en deep learning ; "
    "réponds avec un vocabulaire scientifique et technique."
)

USER_PROMPT = "Qu'est-ce que le surapprentissage ?"

response = chat(
    model=MODEL,
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": USER_PROMPT}
    ],
    stream=False
)

print("=== CONFIGURATION 3 : CHERCHEUR ===")
print(response.message.content)

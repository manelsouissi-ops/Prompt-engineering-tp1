
from ollama import chat

MODEL = "gemma3:4b"

PROMPT = (
    "Propose un nom original pour une application d'aide aux révisions. "
    "Donne uniquement le nom."
)

for num in [20, 60, 150]:
    print(f"\n--- num_predict={num} ---")

    response = chat(
        model=MODEL,
        messages=[{"role": "user", "content": PROMPT}],
        options={
            "temperature": 0.5,
            "num_predict": num
        },
        stream=False
    )

    print("Réponse :", response.message.content)
    print("Tokens générés :", response.eval_count)

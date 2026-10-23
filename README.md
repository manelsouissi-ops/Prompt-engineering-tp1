# TP1 — Prise en main des LLM : API REST, SDK et Python

**Cours :** Prompt Engineering & Agentic AI · **Étudiant :** Aziz Sabri · **Année universitaire :** 2026–2027 · **Encadrante :** Dr. Ing. Rihab Laajili

## Présentation

Ce TP présente plusieurs façons d'interroger des modèles de langage : une API REST locale, le SDK Python d'Ollama et une API hébergée avec GroqCloud. Il explore aussi les messages système et utilisateur, les paramètres de génération et la comparaison de modèles.

### Objectifs

- Comprendre le rôle d'un prompt et structurer une conversation avec des messages.
- Appeler Ollama en HTTP puis avec son SDK Python.
- Observer l'effet des paramètres de génération.
- Comparer Qwen, Gemma et Llama sur une consigne commune.
- Appeler un modèle hébergé avec GroqCloud et protéger la clé API.

## Prérequis

- Python 3.10 ou une version ultérieure
- Visual Studio Code (VS Code)
- Ollama installé et démarré localement
- Les modèles Ollama `qwen3:1.7b`, `gemma3:4b` et `llama3.1:8b`
- Une clé GroqCloud pour l'activité A7

Télécharger les modèles requis dans un terminal :

```bash
ollama pull qwen3:1.7b
ollama pull gemma3:4b
ollama pull llama3.1:8b
```

## Installation

Depuis la racine du projet, créez et activez un environnement virtuel :

```bash
python -m venv .venv
```

Sous Windows PowerShell :

```powershell
.venv\Scripts\Activate.ps1
```

Sous macOS ou Linux :

```bash
source .venv/bin/activate
```

Installez les dépendances :

```bash
python -m pip install -r requirements.txt
```

Pour A7, copiez `.env.example` vers `.env` puis renseignez votre propre clé `GROQ_API_KEY` dans `.env`. Ce fichier local est ignoré par Git : ne partagez pas son contenu.

## Activités et exécution

| Activité | Sujet | Script / exécution |
|---|---|---|
| A1 | Introduction au prompt engineering et préparation de l'environnement LLM. | Activité préparatoire ; aucun script dédié dans les fichiers fournis. |
| A2 | Appel de l'API REST locale d'Ollama avec une requête HTTP. | `python a2_api_rest.py` |
| A3 | Appel d'Ollama avec le SDK Python. | `python a3_sdk_ollama.py` |
| A4 | Structuration des messages `system` et `user` pour guider la réponse. | `python a4_messages.py` |
| A5 | Réglage des paramètres de génération, dont température et limite de tokens. | `python a5_parametres.py` |
| A6 | Comparaison de trois modèles sur la même consigne. | `python a6_comparaison.py` |
| A7 | Appel de GroqCloud avec une clé chargée depuis l'environnement. | `python a7_groq.py` |
| A8 | Synthèse des résultats et rédaction du compte rendu final. | Activité documentée dans le compte rendu ; aucun script A8 fourni. |

Les commandes ci-dessus s'exécutent depuis le dossier du projet. A2 à A6 nécessitent qu'Ollama fonctionne et que le modèle indiqué par le script soit disponible localement. A7 nécessite une clé valide dans `.env` et une connexion Internet.

## Résultats et observations

Les mesures ci-dessous sont les résultats expérimentaux fournis pour la comparaison A6 (250 tokens par modèle) :

| Modèle | Durée | Tokens générés |
|---|---:|---:|
| Qwen3 1.7B | 19,44 s | 250 |
| Gemma3 4B | 30,22 s | 250 |
| Llama3.1 8B | 90,65 s | 250 |

Qwen a été le plus rapide. Gemma a fourni l'explication la plus claire. Llama a mal interprété la consigne. Ces observations décrivent cet essai et cette configuration ; elles ne constituent pas une mesure générale de la qualité des modèles.

### Intégration GroqCloud

Le modèle Groq initialement essayé a renvoyé une erreur HTTP 404. L'implémentation fonctionnelle de A7 utilise `openai/gpt-oss-20b` avec le SDK `groq`.

## Sécurité

- Conservez `GROQ_API_KEY` dans le fichier local `.env` uniquement.
- Ne publiez jamais une clé API, un jeton d'accès ou le contenu de `.env`.
- `.env`, les environnements virtuels, les fichiers Python compilés et les paramètres locaux de VS Code sont ignorés par Git.
- Le fichier `.env.example` ne contient qu'un texte indicatif, aucune clé réelle.

## Compte rendu

Le compte rendu Word demandé (`compte_rendu/Compte_Rendu_TP1_LLM_Aziz_Sabri.docx`) n'était pas présent dans le dossier du projet ni trouvé ailleurs sur le Bureau au moment de la préparation. Il n'est donc pas inclus dans ce dépôt.

## Captures d'écran

Les captures `A6_Comparaison_1.png` et `A6_Comparaison_2.png` n'étaient pas présentes dans le dossier du projet ni trouvées ailleurs sur le Bureau. Aucune capture ni preuve expérimentale n'a été créée artificiellement.

## Conclusion

Ce TP met en pratique l'appel de modèles locaux et distants, la construction de prompts et l'observation de paramètres de génération. Les résultats A6 illustrent un compromis de vitesse et de qualité qui dépend de la tâche et de l'environnement. L'utilisation d'une variable d'environnement pour GroqCloud permet de garder la clé hors du code source.

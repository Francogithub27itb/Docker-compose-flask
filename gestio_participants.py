import json
import re

# Archivo .json que usamos para guardar los participantes
PARTICIPANTS_FILE = "participants.json"

# Regex "básico" para filtrar solo nombres
def validar_nom(nom):
    return bool(re.fullmatch(r"[a-zA-ZÀ-ÿ\s]+", nom))

# Funciones para cargar y guardar los participantes
def carregar_participants():
    try:
        with open(PARTICIPANTS_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def desar_participants(participants):
    with open(PARTICIPANTS_FILE, "w") as f:
        json.dump(participants, f, indent=4)

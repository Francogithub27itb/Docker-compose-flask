import json

# Archivo para llevar las puntuaciones, tambien queria añadir los ganadores de eliminatorias pero por muchos problemas descarto esto
PUNTUACIONS_FILE = "puntuacions.json"

def carregar_puntuacions():
    try:
        with open(PUNTUACIONS_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def actualitzar_puntuacions(guanyador):
    puntuacions = carregar_puntuacions()
    puntuacions[guanyador] = puntuacions.get(guanyador, 0) + 1
    with open(PUNTUACIONS_FILE, "w") as f:
        json.dump(puntuacions, f, indent=4)

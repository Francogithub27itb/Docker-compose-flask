import json
import random

# .json para tratar datos, el .json de torneo no existe por muchos problemas
TORNEIG_FILE = "torneig.json"
PUNTUACIONS_FILE = "puntuacions.json"

def inicialitzar_torneig(mode):
    participants = carregar_participants()
    if mode == "lliga":
        partides = [(a, b) for i, a in enumerate(participants) for b in participants[i+1:]]
    else:  # Eliminatòries
        random.shuffle(participants)
        partides = [(participants[i], participants[i + 1]) for i in range(0, len(participants) - 1, 2)]
        if len(participants) % 2 != 0:
            partides.append((participants[-1], "Descansa"))

    with open(TORNEIG_FILE, "w") as f:
        json.dump({"mode": mode, "partides": partides}, f)

def obtenir_partides():
    try:
        with open(TORNEIG_FILE, "r") as f:
            torneig = json.load(f)
        return torneig.get("partides", [])
    except FileNotFoundError:
        return []

def guardar_resultat(guanyador, partida):
    torneig = json.load(open(TORNEIG_FILE))
    torneig["partides"].remove(partida)

    puntuacions = json.load(open(PUNTUACIONS_FILE))
    puntuacions[guanyador] = puntuacions.get(guanyador, 0) + 1

    with open(TORNEIG_FILE, "w") as f:
        json.dump(torneig, f)

    with open(PUNTUACIONS_FILE, "w") as f:
        json.dump(puntuacions, f)

def reiniciar_torneig():
    open(TORNEIG_FILE, "w").close()
    open(PUNTUACIONS_FILE, "w").close()

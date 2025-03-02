import json
import random
from gestio_participants import carregar_participants
from puntuacions import carregar_puntuacions

# Archivo para guardar la jornada y los partidos de esta.
JORNADA_FILE = "jornada.json"

# Funcion para generar partidos en liga y eliminatorias
def generar_partides(mode):
    participants = carregar_participants()
    if not participants:
        return

    if mode == "lliga":
        partides = [(p1, p2) for i, p1 in enumerate(participants) for p2 in participants[i + 1:]]
    else:  
        random.shuffle(participants)
        partides = [(participants[i], participants[i + 1]) for i in range(0, len(participants) - 1, 2)]
        if len(participants) % 2 != 0:
            partides.append((participants[-1], "Descansa"))

    with open(JORNADA_FILE, "w") as f:
        json.dump({"jornada": 1, "partides": partides}, f)

# Funcion para ir tachando los partidos ya librados
def eliminar_partida(partida_str):
    jornada_actual, partides = obtenir_jornada()
    partides = [p for p in partides if f"{p[0]} vs {p[1]}" != partida_str]
    
    with open(JORNADA_FILE, "w") as f:
        json.dump({"jornada": jornada_actual, "partides": partides}, f)


def obtenir_jornada():
    try:
        with open(JORNADA_FILE, "r") as f:
            jornada_data = json.load(f)
            return jornada_data["jornada"], jornada_data["partides"]
    except (FileNotFoundError, json.JSONDecodeError):
        return 1, []

def avançar_jornada(mode):
    jornada_actual, partides = obtenir_jornada()

    if partides:
        return False  # No podemos avanzar si todavian quedan partidos pendientes

    if mode == "lliga":
        nova_jornada = jornada_actual + 1
        participants = carregar_participants()
        noves_partides = [(p1, p2) for i, p1 in enumerate(participants) for p2 in participants[i + 1:]]

    else:  # Para las eliminatorias
        guanyadors = [p for p in carregar_puntuacions().keys()]
        if len(guanyadors) == 1:
            return f" Campió del torneig: {guanyadors[0]} "
        noves_partides = [(guanyadors[i], guanyadors[i + 1]) for i in range(0, len(guanyadors) - 1, 2)]

    with open(JORNADA_FILE, "w") as f:
        json.dump({"jornada": jornada_actual + 1, "partides": noves_partides}, f)

    return "Torna a l'inici y torna a entrar a /partides"

def reiniciar_torneig():
    with open(JORNADA_FILE, "w") as f:
        json.dump({"jornada": 1, "partides": []}, f)

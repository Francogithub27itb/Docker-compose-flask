from flask import Flask, render_template, request, redirect, url_for, session
from gestio_participants import carregar_participants
from gestio_partides import generar_partides, obtenir_jornada, avançar_jornada, reiniciar_torneig, eliminar_partida
from puntuacions import actualitzar_puntuacions, carregar_puntuacions

app = Flask(__name__)
app.secret_key = "torneig_clau_secreta"

# Ruta para el home del webserver
@app.route("/")
def home():
    return render_template("index.html")

# Ruta para ver/añadir participantes
@app.route("/participants")
def veure_participants():
    participants = carregar_participants()
    return render_template("participants.html", participants=participants)

# Ruta para ver las puntuaciones
@app.route("/puntuacions")
def veure_puntuacions():
    ranking = sorted(carregar_puntuacions().items(), key=lambda x: x[1], reverse=True)
    return render_template("puntuacions.html", ranking=ranking)

# Ruta para interactuar con las partidas
@app.route("/partides", methods=["GET", "POST"])
def veure_partides():
    if request.method == "POST":
        if "mode" in request.form:
            session["mode"] = request.form["mode"]
            session["jornada"] = 1
            generar_partides(session["mode"])
            return redirect(url_for("veure_partides"))

        if "guanyador" in request.form:
            guanyador = request.form["guanyador"]
            partida_str = request.form["partida"]
            eliminar_partida(partida_str)
            actualitzar_puntuacions(guanyador)
            return redirect(url_for("veure_partides"))

        if "avançar" in request.form:
            missatge = avançar_jornada(session["mode"])
            return render_template("partides.html", mode=session["mode"], jornada=session["jornada"], partides=[], missatge=missatge)

    mode = session.get("mode", None)
    jornada, partides = obtenir_jornada()

    return render_template("partides.html", mode=mode, jornada=jornada, partides=partides)

# No es ruta como tal, pero necesario para el botón de reinicio
@app.route("/reiniciar", methods=["POST"])
def reiniciar():
    reiniciar_torneig()
    session.clear()
    return redirect(url_for("veure_partides"))

if __name__ == "__main__":
    app.run(debug=True)

from datetime import datetime

from flask import Flask, abort, jsonify, redirect, render_template, request

try:
    from zoneinfo import ZoneInfo
    FUSEAU = ZoneInfo("Europe/Paris")
except Exception:
    FUSEAU = None

app = Flask(__name__)

COULEURS_AUTORISEES = ["tomato", "teal", "royalblue"]


@app.get("/")
def accueil():
    return render_template("accueil.html")


# ---------------------------------------------------------------
#  Ajoutez vos nouvelles routes ci-dessous 👇
# ---------------------------------------------------------------
@app.get("/presentation")
def presentation():
    return render_template(
        "presentation.html",
        prenom="Ryley",
        nom="Robinson",
        loisirs=["Safe Shallows", "Kelp Forest", "Grassy Plateaus", "Lost River"],
    )


@app.get("/loisirs")
def loisirs():
    return render_template(
        "message.html",
        titre="Loisirs",
        texte="Explorer les biomes, construire des bases et éviter les Reapers.",
    )


@app.get("/bonjour/<prenom>")
def bonjour(prenom):
    return render_template("bonjour.html", prenom=prenom)


@app.get("/calcul")
def calcul():
    a = int(request.args.get("a", 0))
    b = int(request.args.get("b", 0))
    op = request.args.get("op", "plus")
    if op == "fois":
        texte = f"{a} × {b} = {a * b}"
    else:
        texte = f"{a} + {b} = {a + b}"
    return render_template("message.html", titre="Calcul", texte=texte)


@app.get("/formulaire")
def formulaire():
    return render_template("formulaire.html")


@app.route("/salut", methods=["GET", "POST"])
def salut():
    donnees = request.form if request.method == "POST" else request.args
    prenom = donnees.get("prenom", "inconnu")
    ville = donnees.get("ville", "nulle part")
    couleur = donnees.get("couleur", "")
    if couleur not in COULEURS_AUTORISEES:
        couleur = "#00e5ff"
    return render_template(
        "salut.html", prenom=prenom, ville=ville, couleur=couleur,
        methode=request.method,
    )


# --- Exercice 9 : codes de statut ---------------------------------
@app.get("/home")
def home():
    return redirect("/")  # 302 : redirection vers l'accueil


@app.get("/secret")
def secret():
    abort(403)  # accès interdit


@app.errorhandler(403)
def interdit(e):
    return render_template(
        "erreur.html", code=403,
        texte="Zone restreinte : accès refusé, plongeur.",
    ), 403


@app.errorhandler(404)
def introuvable(e):
    return render_template(
        "erreur.html", code=404,
        texte="Cette zone n'existe pas sur 4546B. Vous êtes perdu en mer.",
    ), 404


# --- Exercice 10 : en-têtes HTTP -----------------------------------
@app.get("/moi")
def moi():
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    return render_template(
        "moi.html",
        user_agent=request.headers.get("User-Agent", "inconnu"),
        langues=request.headers.get("Accept-Language", "inconnu"),
        ip=ip,
    )


# --- Exercice 11 : API JSON + JavaScript ----------------------------
@app.get("/api/heure")
def api_heure():
    maintenant = datetime.now(FUSEAU) if FUSEAU else datetime.now()
    return jsonify(
        heure=maintenant.strftime("%H:%M:%S"),
        date=maintenant.strftime("%d/%m/%Y"),
        message="Heure de la base sur 4546B",
    )


@app.get("/horloge")
def horloge():
    return render_template("horloge.html")


# ---------------------------------------------------------------
#  Ne pas modifier : utile seulement pour lancer le site
#  sur votre propre ordinateur (python flask_app.py)
# ---------------------------------------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

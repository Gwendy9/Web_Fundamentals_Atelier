# ---------------------------------------------------------------
#  Mon premier site Web avec Flask
# ---------------------------------------------------------------

from flask import Flask, render_template, request

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
    if request.method == "POST":
        donnees = request.form
    else:
        donnees = request.args
    prenom = donnees.get("prenom", "inconnu")
    ville = donnees.get("ville", "nulle part")
    couleur = donnees.get("couleur", "")
    if couleur not in COULEURS_AUTORISEES:
        couleur = "#00e5ff"
    return render_template(
        "salut.html",
        prenom=prenom,
        ville=ville,
        couleur=couleur,
        methode=request.method,
    )


# ---------------------------------------------------------------
#  Ne pas modifier : utile seulement pour lancer le site
#  sur votre propre ordinateur (python flask_app.py)
# ---------------------------------------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

# On importe la classe Flask depuis la bibliothèque qu'on a installée
from flask import Flask

# On crée l'instance de l'application.
# __name__ permet à Flask de savoir où il se trouve pour trouver les dossiers (templates, static).
app = Flask(__name__)

# Ce décorateur dit à Flask : "Si quelqu'un visite l'adresse '/', exécute la fonction home()"
@app.route('/')
def home():
    # On retourne une simple chaîne de caractères pour tester
    return "CinéLoop Python - Le serveur tourne !"

# Cette condition vérifie si on lance le fichier directement (python app.py)
# Si le fichier est importé par un autre, ce bloc ne s'exécute pas.
if __name__ == '__main__':
    # On démarre le serveur.
    # debug=True active le rechargement automatique (comme nodemon) et les messages d'erreur détaillés.
    # a desactiver en prod
    app.run(debug=True)
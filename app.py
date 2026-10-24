from flask import Flask
# On importe notre fichier db pour déclencher la connexion
import db

app = Flask(__name__)

@app.route('/')
def home():
    # On récupère une connexion au pool
    conn = db.get_connection()
    try:
        # On crée un curseur (c'est l'équivalent de pool.query en Node)
        cur = conn.cursor()
        # On exécute une requête simple
        cur.execute("SELECT COUNT(*) FROM film;")
        # On récupère le résultat
        nombre_films = cur.fetchone()[0]
        cur.close()
        return f"CinéLoop Python - Le serveur tourne ! Il y a {nombre_films} films en base."
    except Exception as e:
        return f"Erreur SQL : {e}"
    finally:
        # On rend TOUJOURS la connexion au pool, même en cas d'erreur
        db.release_connection(conn)

if __name__ == '__main__':
    app.run(debug=True)
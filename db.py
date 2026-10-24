import os
import psycopg2
from psycopg2 import pool
from dotenv import load_dotenv

# On charge les variables depuis le fichier .env
load_dotenv()

# On crée un pool de connexions (minimum 1, maximum 10)
# C'est l'équivalent de "new Pool()" en Node.js
try:
    connection_pool = psycopg2.pool.SimpleConnectionPool(
        1, 10,
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT'),
        database=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD')
    )
    if connection_pool:
        print("Connecté à PostgreSQL")
except Exception as e:
    print(f"Erreur de connexion à PostgreSQL : {e}")
    # force l'arrêt et affiche l'erreur exacte dans la console
    raise e

# Fonction utilitaire pour récupérer une connexion
def get_connection():
    return connection_pool.getconn()

# Fonction utilitaire pour rendre une connexion au pool
def release_connection(conn):
    connection_pool.putconn(conn)
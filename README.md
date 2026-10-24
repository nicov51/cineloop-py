# CinéLoop (Python)

Back-office de gestion de vidéo-club, réécrit en Python avec Flask.

## Prérequis
- Python 3.10+
- Docker (pour la base de données PostgreSQL)

## Installation

### 1. Créer et activer l'environnement virtuel
```bash
python -m venv venv
# Sous Windows PowerShell :
.\venv\Scripts\Activate.ps1
# Sous Windows cmd :
.\venv\Scripts\activate.bat
# Sous Mac/Linux :
source venv/bin/activate
```

### Installer les dependances:
```pip install -r requirements.txt```

### Docker pour la Bdd
``` docker compose up -d db ```
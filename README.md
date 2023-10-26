# flask-api-project

Ce projet est une API Flask qui se connecte à une base de données PostgreSQL pour renvoyer les documents avec le score le plus élevé.

# Installation

## Prérequis :
   - Python 
   - PostgreSQL (pgAdmin4)

## Configuration de l'environnement 
   - les variables d'environnement DB_USER et DB_PASSWORD

## Installation des dépendances :
   bash:
   - pip install flask psycopg2-binary 
   - python -m venv monenv
   - pip install -r requirements.txt 

## Exécution
   Running on http://127.0.0.1:5000/api/topn?n=? 
   n = nombre de documents
## Tests
  - Utilisation unittest : Ces tests vérifient principalement la réponse et le format de la sortie.
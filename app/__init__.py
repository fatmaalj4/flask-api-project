from flask import Flask
from dotenv import load_dotenv
import os

def create_app():
    app = Flask(__name__)

    # Chargement des variables d'environnement depuis .env
    load_dotenv()

    # Enregistrement des routes API
    from app.routes import bp as api_bp
    app.register_blueprint(api_bp, url_prefix="/api")

    return app

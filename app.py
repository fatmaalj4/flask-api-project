# app.py
from flask import Flask

app = Flask(__name__)

def create_app():
    # Configurations et enregistrements d'autres blueprints
    return app

if __name__ == '__main__':
    app.run(debug=True)

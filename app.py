from app import create_app
from app.routes import bp

app = create_app()

if __name__ == "__main__":
    app.run()

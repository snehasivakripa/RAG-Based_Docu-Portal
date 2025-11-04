import os
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    CORS(app, origins=["http://localhost:4200"])

    os.makedirs("./uploads", exist_ok=True)

    # Register blueprints
    from app.routes.data_routes import data_bp
    from app.routes.upload_routes import upload_bp
    from app.routes.query_routes import query_bp

    app.register_blueprint(data_bp, url_prefix="/api")
    app.register_blueprint(upload_bp, url_prefix="/api")
    app.register_blueprint(query_bp, url_prefix="/api")

    return app

from .extensions import db, migrate, login_manager
from .blueprints import register_blueprints
from dotenv import load_dotenv
from flask_cors import CORS
from flask import Flask

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")
    
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # Register blueprints
    register_blueprints(app)
    
    CORS(app, supports_credentials=True, origins=[app.config["FRONTEND_URL"]])
    
    from app import models

    return app
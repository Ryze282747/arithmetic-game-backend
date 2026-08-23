import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    if os.getenv("DB_SSL", "false").lower() == "true":
      SQLALCHEMY_ENGINE_OPTIONS = {
        "connect_args": {
          "ssl": {
            "ca": os.path.join(os.path.dirname(__file__),"ca.pem")
          }
        }
      }
    
    PERMANENT_SESSION_LIFETIME = 3600 * 24 * 30
    SESSION_COOKIE_SAMESITE = os.getenv("SESSION_COOKIE_SAMESITE", "Lax")
    SESSION_COOKIE_SECURE = os.getenv("SESSION_COOKIE_SECURE", "false") == "true"
    
    FRONTEND_URL = os.getenv("FRONTEND_URL")
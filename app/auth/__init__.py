from app.extensions import login_manager, db
from app.models.user import User
from flask import Blueprint

@login_manager.user_loader
def user_loader(user_id):
  return db.session.get(User, user_id)

auth_bp = Blueprint("auth", __name__)

from .routes import *
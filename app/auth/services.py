from flask_login import login_user, current_user
from app.auth.validators import validate_signup
from app.models.user import User
from app.extensions import db
from flask import session
import time

def authenticate(data):
  if current_user.is_authenticated:
    return {"msg":"Already logged in."}, 409
  
  username = data["username"].replace(" ", "")
  password = data["password"].replace(" ", "")
  role = data["role"].replace(" ", "")
  
  user = User.query.filter_by(username=username.lower()).first()
  
  if not user:
    return {"msg":"Invalid credentials."}, 401
  
  isAuthentic = user.check_password(password)
  
  if not isAuthentic:
    return {"msg":"Invalid credentials."}, 401
  
  if role != user.role:
    return {"msg":"Invalid credentials."}, 401
  
  login_user(user, remember=True)
  session.permanent = True
  
  return {
    "msg":"Login successful."
  }, 200

def create_user(data):
  
  error = validate_signup(data)
  
  if error:
    return error
  
  username = data["username"].replace(" ", "")
  password = data["password"].replace(" ", "")
  
  if User.query.filter_by(username=username).first():
    return {
      "msg":"Account already exist."
    }, 409
  
  user = User.from_dict({
    "username": username.lower(), "password": password
  })
  
  db.session.add(user)
  db.session.commit()
  
  return {
    "msg":"Created successfully!",
  }, 201

def get_current_user():
  
  if not current_user.is_authenticated:
    return {
      "authenticated": False
    }, 401
  
  return {
    "authenticated":True,
    "user":current_user.to_dict()
  }, 200
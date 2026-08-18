from app.auth.services import authenticate, create_user, get_current_user
from flask_login import logout_user
from flask import request, jsonify
from . import auth_bp

@auth_bp.route("/login", methods=["POST"])
def login():
  
  data = request.get_json()
  
  res, status = authenticate(data)
  
  return jsonify(res), status
  
@auth_bp.route("/signup", methods=["POST"])
def signup():
  
  data = request.get_json()
  
  res, status = create_user(data)
  
  return jsonify(res), status

@auth_bp.route("/logout", methods=["POST"])
def logout():
  logout_user()
  
  return {"msg":"Successfully logged out."}, 200

@auth_bp.route("/me")
def me():
  res, status = get_current_user()
  return jsonify(res), status
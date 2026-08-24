from app.decorators.auth import student_required
from .services import create_new_quiz
from flask_login import login_required
from flask import jsonify, request
from . import game_bp

@game_bp.route("/quiz", methods=["POST"])
@login_required
@student_required
def quiz():
  data = request.get_json()
  
  res, status = create_new_quiz(data)
  
  return jsonify(res), status

@game_bp.route("/answers", methods=["POST"])
def answers():
  data = request.get_json()
  
  print(data)
  
  return {
    "correct_ans":10, 
    "num_qs":10, 
    "score":100
  }, 200
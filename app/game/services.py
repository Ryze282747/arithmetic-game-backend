from .validators import validate_game_data
from .generators import generate_questions
from app.models.quiz import Quiz
from app.extensions import db
from flask import session

def create_new_quiz(data):
  
  valid, error = validate_game_data(data)
  
  if not valid:
    return {"error":error}, 400
  
  if session.get("quiz", None):
    delete_quiz(session["quiz"])
    session.pop("quiz")
  
  quiz = Quiz.from_obj(data)
  
  db.session.add(quiz)
  db.session.flush()
  
  questions = generate_questions(quiz)
  
  db.session.commit()
  
  session["quiz"] = quiz.id
  
  return {"questions":questions}, 200

def delete_quiz(quiz_id):
  quiz = Quiz.query.get(quiz_id)
  
  if not quiz:
    return None
  
  db.session.delete(quiz)
  db.session.commit()
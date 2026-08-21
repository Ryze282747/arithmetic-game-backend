from .validators import validate_game_data
from .generators import generate_questions
from app.models.quiz import Quiz
from app.extensions import db

def create_new_quiz(data):
  
  valid, error = validate_game_data(data)
  
  if not valid:
    return {"error":error}, 400
  
  quiz = Quiz.from_obj(data)
  
  db.session.add(quiz)
  db.session.flush()
  
  questions = generate_questions(quiz)
  
  db.session.commit()
  
  return {"questions":questions}, 200
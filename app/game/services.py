from app.models import QuizAttempt, Question, Quiz
from .validators import validate_game_data, validate_answers
from .generators import generate_questions
from .helpers import get_total_score
from app.extensions import db
from flask import session

def create_new_quiz(data):
  
  valid, error = validate_game_data(data)
  
  if not valid:
    return {"error":error}, 400
  
  if session.get("quiz", None):
    delete_quiz(session["quiz"])
    session.pop("quiz")
  
  quiz = Quiz.from_dict(data)
  
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

def process_answers(data):
  
  valid, error = validate_answers(data)
  
  if not valid:
    return {"error":error}, 400
  
  answers = data["answers"]
  time = data["time"]
  
  quiz = Quiz.query.filter_by(id=session.get("quiz")).first()
  
  if not quiz:
    return {"msg":"Quiz not found"}, 404
  
  total_questions, correct_answers, raw_scores = check_answers(answers)
  
  total_score = get_total_score(raw_scores, quiz)
  
  attempt_data = {
    "score": total_score,
    "time": time,
    "correct_answers": correct_answers,
    "total_questions": total_questions,
    "operation": quiz.operation,
    "difficulty": quiz.difficulty
  }
  
  attempt = QuizAttempt.from_dict(attempt_data)
  
  db.session.add(attempt)
  db.session.delete(quiz)
  db.session.commit()

  return {
    "correct_ans":correct_answers, 
    "total_questions":total_questions, 
    "score":total_score,
    "time":time
  }, 200

def check_answers(answers):
  
  total_questions = len(answers)
  correct_answers = 0
  raw_scores = []
  
  for qid in answers:
    question = Question.query.filter_by(id=qid).first()
    if question.check_answer(answers[qid]):
      correct_answers += 1
      raw_scores.append(1)
    
  
  return total_questions, correct_answers, raw_scores
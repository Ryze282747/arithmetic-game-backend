from .helpers import get_range, get_number_from_range, get_question, get_answer, get_choices
from app.models import Question
from app.extensions import db

def generate_questions(quiz):
  
  questions_obj = []
  questions = []
  
  while len(questions) != 10:
    question_obj, question = generate_question(quiz.operation, quiz.difficulty, quiz.id)
    
    if question not in questions:
      questions.append(question)
      questions_obj.append(question_obj)
  
  for obj in questions_obj:
    db.session.add(obj)
  
  db.session.flush()
  
  return [obj.to_dict() for obj in questions_obj]

def generate_question(operation, difficulty, quiz_id):
  
  number_range = get_range(difficulty)
  
  num1 = get_number_from_range(number_range)
  num2 = get_number_from_range(number_range)
  
  question = get_question(num1, num2, operation)
  answer = get_answer(num1, num2, operation)
  
  choices = get_choices(number_range, answer)
  
  data = {
    "quiz_id":quiz_id, "question":question,
    "choice_1":choices[0], "choice_2":choices[1],
    "choice_3":choices[2], "choice_4":choices[3],
    "correct_answer":answer
  }
  
  question_obj = Question.from_dict(data)
  
  return question_obj, question
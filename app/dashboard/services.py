from .helpers import get_total_points, get_best_time, get_accuracy
from flask_login import current_user
from app.models import QuizAttempt

def get_student_dashboard():
  
  attempts = QuizAttempt.query.filter_by(user_id=current_user.id).all()
  
  if len(attempts) == 0:
    return {
      "best_time": 0,
      "quiz_taken": 0,
      "accuracy": 0,
      "total_points": 0
    }, 200
  
  total_points = get_total_points(attempts)
  best_time = get_best_time(attempts)
  accuracy = get_accuracy(attempts)
  
  return {
    "best_time": best_time,
    "quiz_taken": len(attempts),
    "accuracy": accuracy,
    "total_points": total_points
  }, 200

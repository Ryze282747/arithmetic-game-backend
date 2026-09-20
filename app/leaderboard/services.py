from flask_login import current_user
from app.models import User
import time

def get_leaderboard():
  
  users = User.query.all()
  
  users_total_points = []
  
  for user in users:
    
    if user.role == "student":
      scores = [attempt.score for attempt in user.quiz_attempts]
    
      users_total_points.append({
        "name": user.username.capitalize(),
        "points": sum(scores)
      })
  
  top_scores = sorted(users_total_points, key=lambda item: item["points"], reverse=True)[:10]
  
  return {
    "data":top_scores
  }, 200
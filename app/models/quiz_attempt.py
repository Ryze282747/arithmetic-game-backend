from flask_login import current_user
from app.extensions import db
from datetime import datetime
import uuid

class QuizAttempt(db.Model):
  __tablename__ = "quiz_attempts"
  
  id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False)
  
  user_id = db.Column(db.String(36), db.ForeignKey("users.id"), nullable=False)
  
  score = db.Column(db.Integer, nullable=False)
  time = db.Column(db.Float, nullable=False)
  correct_answers = db.Column(db.Integer, nullable=False)
  total_questions = db.Column(db.Integer, nullable=False)
  date_taken = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  
  user = db.relationship("User", back_populates="quiz_attempts")
  
  @classmethod
  def from_dict(cls, obj):
    return cls(
      score=obj["score"],
      time=obj["time"],
      correct_answers=obj["correct_answers"],
      total_questions=obj["total_questions"],
      user=current_user,
    )
  
  def to_dict(self):
    return {
      "score":self.score,
      "time":self.time,
      "correct_answers":self.correct_answers,
      "total_questions":self.total_questions,
      "date_taken":self.date_taken
    }
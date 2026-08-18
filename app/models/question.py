from app.extensions import db
import uuid

class Question(db.Model):
  __tablename__ = "questions"
  
  id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False)
  
  quiz_id = db.Column(db.String(36), db.ForeignKey("quizzes.id"), nullable=False)
  
  question = db.Column(db.String(255), nullable=False)
  
  choice_1 = db.Column(db.String(50), nullable=False)
  choice_2 = db.Column(db.String(50), nullable=False)
  choice_3= db.Column(db.String(50), nullable=False)
  choice_4 = db.Column(db.String(50), nullable=False)
  
  correct_answer = db.Column(db.String(50), nullable=False)
  
  quiz = db.relationship(
    "Quiz",
    back_populates="questions"
  )
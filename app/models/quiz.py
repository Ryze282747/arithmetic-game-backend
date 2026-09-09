from app.extensions import db
import uuid

class Quiz(db.Model):
  __tablename__ = "quizzes"
  
  id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False)
  
  operation = db.Column(db.String(50), nullable=False)
  difficulty = db.Column(db.String(50), nullable=False)
  
  questions = db.relationship(
    "Question",
    back_populates="quiz",
    cascade="all, delete-orphan"
  )
  
  @classmethod
  def from_dict(cls, obj):
    return cls(
      operation=obj["operation"],
      difficulty=obj["difficulty"],
    )
  
  def to_dict(self):
    return {
      "operation":self.operation,
      "difficulty":self.difficulty,
      "questions":[question.to_dict() for question in self.questions]
    }
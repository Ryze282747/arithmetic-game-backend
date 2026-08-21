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
  
  @classmethod
  def from_dict(cls, obj):
    return cls(
      quiz_id=obj["quiz_id"],
      question=obj["question"],
      choice_1=obj["choice_1"],
      choice_2=obj["choice_2"],
      choice_3=obj["choice_3"],
      choice_4=obj["choice_4"],
      correct_answer=obj["correct_answer"],
    )
  
  def to_dict(self):
    return {
      "question_id":self.id,
      "question":self.question,
      "choices": [self.choice_1, self.choice_2, self.choice_3, self.choice_4],
    }
  
  def check_answer(self, user_ans):
    return int(self.correct_answer) == int(user_ans)
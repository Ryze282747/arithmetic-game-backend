from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from app.extensions import db
import uuid

class User(UserMixin, db.Model):
  __tablename__ = "users"
  
  id = db.Column(db.String(36), nullable=False, default=lambda: str(uuid.uuid4()), primary_key=True)
  
  username = db.Column(db.String(255), nullable=False, unique=True)
  
  password = db.Column(db.String(255), nullable=False)
  
  role = db.Column(db.String(20), nullable=False, default="student")
  
  quiz_attempts = db.relationship("QuizAttempt", back_populates="user")
  
  @staticmethod
  def hash_password(password):
    return generate_password_hash(password)
  
  @classmethod
  def from_dict(cls, obj):
    return cls(
      username=obj["username"],
      password=cls.hash_password(obj["password"]),
    )
  
  def to_dict(self):
    return {
      "username":self.username,
      "id":self.id,
      "role":self.role
    }
  
  def check_password(self, plain_password):
    return check_password_hash(self.password, plain_password)
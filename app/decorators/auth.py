from functools import wraps
from flask import jsonify
from flask_login import current_user


def admin_required(view):
  @wraps(view)
  def wrapped_view(*args, **kwargs):
    
    if current_user.role != "admin":
      return jsonify({
        "error": "Admin access required"
      }), 403
    return view(*args, **kwargs)
    
  return wrapped_view

def student_required(view):
  @wraps(view)
  def wrapped_view(*args, **kwargs):
    
    if current_user.role != "student":
      return jsonify({
        "error": "Student access required"
      }), 403
    return view(*args, **kwargs)
  
  return wrapped_view
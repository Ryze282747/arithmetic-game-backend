from .services import get_leaderboard
from . import leaderboard_bp
from flask import jsonify

@leaderboard_bp.route("/")
def leaderboard():
  
  data, status = get_leaderboard()
  
  return jsonify(data), status

from app.decorators.auth import admin_required, student_required
from flask_login import login_required
from . import dashboard_bp 
from flask import jsonify

@dashboard_bp.route("/student")
@login_required
@student_required
def student_dashboard():
  return jsonify({"msg":"Test"}), 200
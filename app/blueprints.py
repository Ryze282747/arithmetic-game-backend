def register_blueprints(app):
  from .auth import auth_bp
  from .dashboard import dashboard_bp
  from .game import game_bp
  from .leaderboard import leaderboard_bp
  
  app.register_blueprint(auth_bp, url_prefix="/auth")
  app.register_blueprint(dashboard_bp, url_prefix="/dashboard")
  app.register_blueprint(game_bp, url_prefix="/game")
  app.register_blueprint(leaderboard_bp, url_prefix="/leaderboard")
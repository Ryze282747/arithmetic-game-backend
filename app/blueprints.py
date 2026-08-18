def register_blueprints(app):
  from .auth import auth_bp
  from .dashboard import dashboard_bp
  
  app.register_blueprint(auth_bp, url_prefix="/auth")
  app.register_blueprint(dashboard_bp, url_prefix="/dashboard")
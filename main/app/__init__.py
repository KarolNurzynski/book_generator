from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_filename=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(config_filename)
    initialize_extensions(app)
    register_blueprints(app)
    with app.app_context():
        db.create_all()
    return app

def initialize_extensions(app):
    db.init_app(app)

def register_blueprints(app):
    from app.module.group.book import book_blueprint
    app.register_blueprint(book_blueprint)
    


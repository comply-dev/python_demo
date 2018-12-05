from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import event

db = SQLAlchemy()
db.event = event


def init_app(app):
    db.init_app(app)
    return app


def init_db(drop=False):
    if drop:
        db.drop_all()
    db.create_all()

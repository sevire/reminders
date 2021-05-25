from flask import Flask
from flask import current_app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app():
    """Construct the core application."""
    new_app = Flask(__name__, instance_relative_config=False)
    new_app.config.from_object('config.Config')

    db.init_app(new_app)

    with new_app.app_context():
        # from . import routes  # Import routes
        db.create_all()  # Create sql tables for our data models

        return new_app


@current_app.route('/')
def hello_world():
    return 'Hello World!'


@current_app.route('/mail')
def process_mail():
    return "You have mail"


if __name__ == '__main__':
    app = init_app()
    app.run()

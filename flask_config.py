class FlaskConfig:
    """Set Flask configuration from .env file."""

    # General Config
    SECRET_KEY = "replacewithpropersecretkeyforproduction"
    FLASK_APP = "app.py"
    FLASK_ENV = "Production"
    FLASK_DEBUG = 3

    # Database
    SQLALCHEMY_DATABASE_URI ="sqlite:///reminder.db"
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

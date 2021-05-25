from flask import Flask
from html_utilities import table
from database import User, Alert, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reminders.db'

db.init_app(app)


@app.route('/users')
def list_users():
    users = User.query.all()
    users_html = table(['username', 'email'], users)
    return users_html


@app.route('/alerts')
def process_mail():
    alerts = Alert.query.all()
    alerts_html = table(['id', 'message', 'issue_time'], alerts)
    return alerts_html


if __name__ == '__main__':
    app.run()

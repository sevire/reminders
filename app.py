from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from html_utilities import table

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reminders.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username!r}>'


class ReminderAlert(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(300), nullable=False)
    issue_time = db.Column(db.DateTime(), nullable=False)

    def __repr__(self):
        return f'<ReminderAlert {id}: {self.message!r}: {self.issue_time!r}'


@app.route('/users')
def list_users():
    users = User.query.all()
    users_html = table(['username', 'email'], users)
    return users_html


@app.route('/alerts')
def process_mail():
    alerts = ReminderAlert.query.all()
    alerts_html = table(['id', 'message', 'issue_time'], alerts)
    return alerts_html


if __name__ == '__main__':
    app.run()

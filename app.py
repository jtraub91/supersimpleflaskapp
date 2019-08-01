import os
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

class Config(object):
    SECRET_KEY = 'super-duper-secret-key'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///app.db'


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    string = db.Column(db.String(240), default='', nullable=False)

    def __repr__(self):
        return "<Entry_{}>".format(self.id)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        entries = Entry.query.all()
        entry_list = [e.string for e in entries]
        return render_template("index.html", entry_list=entry_list)
    elif request.method == 'POST':
        entry = Entry(string=request.form['string'])
        db.session.add(entry)
        db.session.commit()
        return redirect("/")


if __name__ == '__main__':
    app.run()


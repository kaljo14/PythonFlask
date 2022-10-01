from ast import dump
from crypt import methods
from pickle import TRUE
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from pprint import pprint
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/barber_shop'
db = SQLAlchemy(app)


class barbers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    description = db.Column(db.String())
    image = db.Column(db.String())
    status = db.Column(db.String())
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<barbers:{self.name}>'


@app.route('/', methods=['GET', 'POST'])
def index():

    barber = barbers.query.all()
    return render_template('index.html', barber=barber)


if __name__ == "__main__":
    app.run(debug=True)

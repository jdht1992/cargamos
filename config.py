from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'this-really-needs-to-be-changed'
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://jdht:@localhost/cargamos'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# initialize the database connection
db = SQLAlchemy(app)

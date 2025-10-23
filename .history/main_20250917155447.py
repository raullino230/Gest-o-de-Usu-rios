from flask import Flask
from configuration import configure_all
from database.models.cliente import Cliente
from database.database import db


app = Flask(__name__)

db.connect()
db.create_tables([Cliente])

configure_all(app)


app.run(debug=True)
from flask import Flask
from configuration import configure_all
from database.models.cliente import Cliente
from database.database import db


app = Flask(__name__)

import os

# Apaga o banco antigo se existir
if os.path.exists('custemermanager.db'):
	os.remove('custemermanager.db')
db.connect()
db.create_tables([Cliente])

configure_all(app)


app.run(debug=True)
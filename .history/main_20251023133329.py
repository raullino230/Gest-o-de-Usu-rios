from flask import Flask
from configuration import configure_all
from database.models.cliente import Cliente
from database.database import db

import os

# Remover o banco apenas se explicitamente solicitado
os.remove(os.path.join(os.path.dirname(__file__), 'custemermanager.db'))

app = Flask(__name__)

db.connect()
db.create_tables([Cliente])

configure_all(app)


app.run(debug=True)
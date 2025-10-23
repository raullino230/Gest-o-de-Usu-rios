from flask import Flask
from configuration import configure_all
from flask import Flask
from database.models.cliente import Cliente
from database.database import db

db.connect()
db.create_tables([Cliente])

# ...restante do seu código Flask...

 


app = Flask(__name__)

configure_all(app)


app.run(debug=True)
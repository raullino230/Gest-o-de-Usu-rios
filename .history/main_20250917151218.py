from flask import Flask
from configu

 


app = Flask(__name__)

configure_all(app)


app.run(debug=True)
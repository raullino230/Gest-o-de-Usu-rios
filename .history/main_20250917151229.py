from flask import Flask
from configura

 


app = Flask(__name__)

configure_all(app)


app.run(debug=True)
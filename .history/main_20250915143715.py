from flask import Flask
from routes.home import home_route


app = Flask(__name__)

app

app.run(debug=True)
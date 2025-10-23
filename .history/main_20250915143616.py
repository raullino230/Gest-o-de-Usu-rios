from flask import Flask
from routes.home import home_

app = Flask(__name__)

app.run(debug=True)
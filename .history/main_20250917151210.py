from flask import Flask


 


app = Flask(__name__)

configure_all(app)


app.run(debug=True)
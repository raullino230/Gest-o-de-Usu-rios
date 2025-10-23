from flask import Flask

 


app = Flask(__name__)

configure_all(app)

app.register_blueprint(home_route)
app.register_blueprint(cliente_route)


app.run(debug=True)
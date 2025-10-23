from flask import Blueprint

cliente_route = Blueprint('cliente', __name__)

@home_route.route('/')
def home():
    return render_template('index.html')
from flask import Blueprint, render_template
from database.models.cliente import Cliente

home_route = Blueprint('home', __name__)

@home_route.route('/')
def home():
    clientes = Cliente.select()
    return render_template('index.html', clientes=clientes)
from flask import Blueprint, render_template

cliente_route = Blueprint('cliente', __name__)

@cliente_route.route('/')
def lista_cliente():
    pass


@cliente_route.route('/')
def lista_ciente():
    pass
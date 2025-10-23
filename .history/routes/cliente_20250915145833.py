from flask import Blueprint

cliente_route = Blueprint('cliente', __name__)


@cliente_route.route('/')
def lista_cliente():
    pass


@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    pass

@cliente_route.route('/new')
def form_cliente():    
    pass

@cliente_route.route('/<int:cliente')
def detalhe_cliente():
    pass
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

@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
    pass

@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
    pass

@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
    pass

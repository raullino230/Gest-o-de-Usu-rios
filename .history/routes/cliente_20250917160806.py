from flask import Blueprint, render_template, request
from database.models.cliente import Cliente



cliente_route = Blueprint('cliente', __name__)


@cliente_route.route('/cliente')
def lista_template():

    clientes = Cliente.select()
    return render_template('lista_template.html', clientes=clientes)


@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    nome = request.form.get('nome')
    email = request.form.get('email')
    existe = Cliente.select().where((Cliente.nome == nome) | (Cliente.email == email)).exists()
    if existe:
        erro = 'Nome ou email já cadastrado!'
        clientes = Cliente.select()
        return render_template('index.html', clientes=clientes, erro=erro)
    Cliente.create(nome=nome, email=email)
    clientes = Cliente.select()
    return render_template('index.html', clientes=clientes)
    

    

@cliente_route.route('/new')
def form_cliente():    
    return render_template('form_cliente.html')


@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):


    cliente = Cliente.get_by_id(cliente_id)
    return render_template('detalhe_cliente.html', cliente=cliente)


@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
    cliente = Cliente.get_by_id(cliente_id)
    clientes = Cliente.select()
    return render_template('index.html', clientes=clientes, cliente=cliente)


@cliente_route.route('/<int:cliente_id>/update', methods=['POST'])
def atualizar_cliente(cliente_id):
    nome = request.form.get('nome')
    email = request.form.get('email')
    cliente = Cliente.get_by_id(cliente_id)
    cliente.nome = nome
    cliente.email = email
    cliente.save()
    clientes = Cliente.select()
    return render_template('index.html', clientes=clientes)


@cliente_route.route('/<int:cliente_id>/delete', methods=['POST'])
def delete_cliente(cliente_id):
    cliente = Cliente.get_by_id(cliente_id)
    cliente.delete_instance()
    clientes = Cliente.select()
    return render_template('index.html', clientes=clientes)

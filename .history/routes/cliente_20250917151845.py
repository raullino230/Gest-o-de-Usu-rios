from flask import Blueprint, render_template, request, json, redirect, url_for
from database.cliente import CLIENTES
from database.models.cliente import Cliente



cliente_route = Blueprint('cliente', __name__)


@cliente_route.route('/cliente')
def lista_template():

    clientes = Cliente.select()
    return render_template('lista_template.html', clientes=)


@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    nome = request.form.get('nome')
    email = request.form.get('email')
    existe = any(c['nome'] == nome or c['email'] == email for c in CLIENTES)
    if existe:
        erro = 'Nome ou email já cadastrado!'
        return render_template('index.html', clientes=CLIENTES, erro=erro)
    novo_id = max([c['id'] for c in CLIENTES]) + 1 if CLIENTES else 1
    CLIENTES.append({'id': novo_id, 'nome': nome, 'email': email})    
    return render_template('index.html', clientes=CLIENTES)
    

    

@cliente_route.route('/new')
def form_cliente():    
    return render_template('form_cliente.html')


@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):


    cliente = list(filter(lambda c: c['id'] == cliente_id, CLIENTES))[0]
    return render_template('detalhe_cliente.html', cliente=cliente)


@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
    cliente = None
    for c in CLIENTES:
        if c['id'] == cliente_id:
            cliente = c
            break
    return render_template('index.html', clientes=CLIENTES, cliente=cliente)


@cliente_route.route('/<int:cliente_id>/update', methods=['POST'])
def atualizar_cliente(cliente_id):
    nome = request.form.get('nome')
    email = request.form.get('email')
    #OBTER O USUARIO PELO ID
    for c in CLIENTES:
        if c['id'] == cliente_id:
            c['nome'] = nome
            c['email'] = email
            break
    #EDITAR USUARIO
    return render_template('index.html', clientes=CLIENTES)


@cliente_route.route('/<int:cliente_id>/delete', methods=['POST'])
def delete_cliente(cliente_id):
    global CLIENTES
    CLIENTES = [c for c in CLIENTES if c['id'] != cliente_id]
    return render_template('index.html', clientes=CLIENTES)

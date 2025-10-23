from flask import Flask, url_for, render_template

#inicialização
app = Flask(__name__)

#rotas
@app.route("/")
def ola_mundo():
    titulo = "Gestão de Usuarios"
    usuarios = [
        {"nome": "Raul Lucas", "membro_ativo": True},
        {"nome": "Livia Alves", "membro_ativo": False},
        {"nome": "Lucineia Alves", "membro_ativo": True},
        {"nome": "Ricardo Lino", "membro_ativo": F},
    ]
    
    return render_template('index.html', titulo=titulo, usuarios=usuarios)

@app.route("/sobre")
def pagina_sobre():
    return """"    
     <a href=https://www.youtube.com/watch?v=fkXlSyWiXVg&list=PLC85vCGMW9rRm4HzhLGUSxdYfy5Mys-Xx&index=31>video legal</a>


"""

#Execução
app.run(debug=True)
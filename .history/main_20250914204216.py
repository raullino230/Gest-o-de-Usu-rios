from flask import Flask, url_for, render_template

#inicialização
app = Flask(__name__)

#rotas
@app.route("/")
def ola_mundo():
    titulo = "Gestão de Usuarios"
    usuarios = {
        {"Nome:" "Raul Lucas" "Membro_Ativo": True},
        {"Nome:" "Livia Alves" "Membro_Ativo": False},
        {"Nome:" "Lucineia Alves" "Membro_Ativo": True},
        {"Nome:" "Ricardo Lino" "Membro_Ativo": True},
    }
    return render_template('index.html', titulo=titulo )

@app.route("/sobre")
def pagina_sobre():
    return """"    
     <a href=https://www.youtube.com/watch?v=fkXlSyWiXVg&list=PLC85vCGMW9rRm4HzhLGUSxdYfy5Mys-Xx&index=31>video legal</a>


"""

#Execução
app.run(debug=True)
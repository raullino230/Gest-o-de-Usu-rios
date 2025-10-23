from flask import Flask

#inicialização
app = Flask(__name__)

#rotas
@app.route('/')
def ola_mundo():
    return "coé da boa?"

@app.route("/sobre")
def pagina_sobre():
    return """"
    


"""

#Execução
app.run(debug=True)
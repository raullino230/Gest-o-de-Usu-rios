from flask import Flask

#inicialização
app = Flask(__name__)

#rotas
@app.route('/')
def ola_mundo():
    return "coé da boa?"

@app.router("/sobre")
def pagina_sobre():
    return ("<raul é lindo gostoso")

#Execução
app.run(debug=True)
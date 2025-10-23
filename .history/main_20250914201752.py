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
     href="https://www.youtube.com/watch?v=fkXlSyWiXVg&list=PLC85vCGMW9rRm4HzhLGUSxdYfy5Mys-Xx&index=31"


"""

#Execução
app.run(debug=True)
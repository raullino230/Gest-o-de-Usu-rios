from flask import Flask, url_for

#inicialização
app = Flask(__name__)

#rotas
@app.route("/")
def ola_mundo():
    return f"<a href='{url_for('pagina_sobre')}'>pagina"

@app.route("/sobre")
def pagina_sobre():
    return """"    
     <a href=https://www.youtube.com/watch?v=fkXlSyWiXVg&list=PLC85vCGMW9rRm4HzhLGUSxdYfy5Mys-Xx&index=31>video legal</a>


"""

#Execução
app.run(debug=True)
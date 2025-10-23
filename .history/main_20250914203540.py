from flask import Flask, url_for, render_template

#inicialização
app = Flask(__name__)

#rotas
@app.route("/")
def ola_mundo():
    titulo = "GEstão de Usua"
    return render_template('index.html')

@app.route("/sobre")
def pagina_sobre():
    return """"    
     <a href=https://www.youtube.com/watch?v=fkXlSyWiXVg&list=PLC85vCGMW9rRm4HzhLGUSxdYfy5Mys-Xx&index=31>video legal</a>


"""

#Execução
app.run(debug=True)
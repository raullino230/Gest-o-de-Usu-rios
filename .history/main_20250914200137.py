from flask import Flask

#inicialização
app = Flask(__name__)

#rotas
@app.route('/')


#Execução
app.run(debug=True)
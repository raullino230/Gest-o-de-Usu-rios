from flask import Flask, url_for, render_template

#inicialização
app = Flask(__name__)

#Execução
app.run(debug=True)
from flask import Flask
from configuration import configure_all
import os


# Nota: a configuração do banco (connect/create_tables) já é feita em configuration.configure_db()
# Evita-se chamar db.connect() aqui para não abrir a conexão duas vezes.

app = Flask(__name__)

# Remover o banco apenas se a variável de ambiente REMOVE_DB estiver definida (evita remoção acidental)
if os.environ.get('REMOVE_DB') in ('1', 'true', 'True'):
	db_path = os.path.join(os.path.dirname(__file__), 'custemermanager.db')
	if os.path.exists(db_path):
		os.remove(db_path)

configure_all(app)


app.run(debug=True)
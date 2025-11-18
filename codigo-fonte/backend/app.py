
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

# --- CONFIGURAÇÃO ---
app = Flask(__name__)

# Configuração do Banco de Dados MySQL
# (Corresponde ao seu script SQL e ao que você disse ao professor)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:sua_senha_aqui@localhost/pites_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa o banco de dados com o app
db = SQLAlchemy(app)

# Importa os controllers (nossa lógica) e os models (nossas tabelas)
# Fazemos isso *depois* de inicializar o 'db'
from models.tarefa import Tarefa
from controllers.tarefa_controller import TarefaController

# --- ROTAS (O "Roteador" do MVC) ---

@app.route('/')
def index():
    """ Rota principal que lista as tarefas. """
    # Simula a chamada ao controller
    # Em um app real, o controller buscaria os dados
    tarefas_simuladas = [
        {'titulo': 'Gravar vídeo PITES', 'status': 'pendente'},
        {'titulo': 'Entregar atividade', 'status': 'pendente'},
    ]
    # No vídeo, você explica que esta rota renderiza o 'frontend/index.html'
    return render_template('index.html', tarefas=tarefas_simuladas)


@app.route('/criar_tarefa', methods=['POST'])
def criar_tarefa():
    """ Rota que recebe dados para criar uma tarefa. """
    if request.method == 'POST':
        titulo = request.form['titulo']
        
        # 1. Chama o Controller para a lógica de negócios
        TarefaController.criar(db=db, titulo=titulo, usuario_id=1) # Simula usuário 1
        
        # 2. Redireciona de volta para a lista
        return redirect(url_for('index'))

# --- EXECUÇÃO ---
if __name__ == '__main__':
    # Cria as tabelas no banco de dados (se não existirem)
    with app.app_context():
        db.create_all()
    # Roda o servidor
    app.run(debug=True)

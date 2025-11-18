
from flask_sqlalchemy import SQLAlchemy
from app import db # Importamos o 'db' que foi inicializado no app.py

# Modelo da Tabela Tarefa (baseado no seu script SQL)
class Tarefa(db.Model):
    __tablename__ = 'Tarefas' # Nome exato da tabela no MySQL
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(150), nullable=False)
    descricao = db.Column(db.Text, nullable=True)
    status = db.Column(db.Enum('pendente', 'concluida'), default='pendente')
    # Não precisamos da data_criacao ou usuario_id agora para simplificar
    
    def __repr__(self):
        return f'<Tarefa {self.titulo}>'

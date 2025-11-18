from app import db # Importamos o 'db' que foi inicializado no app.py
from sqlalchemy.sql import func # Para pegar a data atual

class Tarefa(db.Model):
    __tablename__ = 'Tarefas' # Nome exato da tabela no MySQL
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(150), nullable=False)
    descricao = db.Column(db.Text, nullable=True)
    status = db.Column(db.Enum('pendente', 'concluida'), default='pendente', nullable=False)
    
    # Campo de data (combinando com o SQL)
    data_criacao = db.Column(db.DateTime(timezone=True), server_default=func.now())
    
    # Chave Estrangeira (combinando com o SQL)
    usuario_id = db.Column(db.Integer, db.ForeignKey('Usuarios.id'), nullable=False)

    def __repr__(self):
        return f'<Tarefa {self.titulo}>'

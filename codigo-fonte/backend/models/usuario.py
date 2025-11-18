
from app import db # Importamos o 'db' que foi inicializado no app.py

class Usuario(db.Model):
    __tablename__ = 'Usuarios' # Nome exato da tabela no MySQL
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(255), nullable=False) # No app real, isso seria hash
    
    # Define o relacionamento: Um Usuário tem muitas Tarefas
    tarefas = db.relationship('Tarefa', backref='usuario', lazy=True)

    def __repr__(self):
        return f'<Usuario {self.nome}>'

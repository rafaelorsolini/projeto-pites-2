
# Padrão MVC - Controller
# /backend/controllers/tarefa_controller.py

from models.tarefa import Tarefa # Importa o Modelo

class TarefaController:
    
    @staticmethod
    def criar(db, titulo, usuario_id):
        """
        Método estático para criar uma nova tarefa.
        No vídeo, você explica que o Controller:
        1. Recebe os dados da Rota (app.py).
        2. Valida os dados (ex: IF para checar se o título não está vazio).
        3. Cria o objeto do Modelo (Tarefa).
        4. Salva no banco de dados (db.session.add / db.session.commit).
        """
        
        # Simulação da lógica de validação e criação
        print(f"CONTROLLER: Validando e criando tarefa '{titulo}'...")
        
        # Lógica real (simulada):
        # if not titulo:
        #    raise ValueError("Título não pode ser vazio")
        #
        # nova_tarefa = Tarefa(titulo=titulo, usuario_id=usuario_id)
        # db.session.add(nova_tarefa)
        # db.session.commit()
        
        print("CONTROLLER: Tarefa salva no banco (simulado).")
        return True

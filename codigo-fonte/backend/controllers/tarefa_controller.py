
# Padrão MVC - Controller
# /backend/controllers/tarefa_controller.py

class TarefaController:
    
    def __init__(self, model):
        # Em um app real, injetaríamos o Model (banco de dados)
        self.model = model 

    def listar_tarefas(self, usuario_id):
        """
        Método para listar tarefas (simulação)
        """
        print(f"CONTROLADOR: Buscando tarefas para o usuário: {usuario_id}")
        # ... aqui viria a lógica para chamar o self.model
        pass

    def criar_tarefa(self, titulo, usuario_id):
        """
        Método para criar tarefa (simulação)
        """
        print(f"CONTROLADOR: Criando tarefa '{titulo}' para o usuário {usuario_id}")
        # ... aqui viria a lógica de validação
        # ... e depois chamaria o self.model.salvar(titulo, usuario_id)
        pass

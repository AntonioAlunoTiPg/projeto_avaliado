from app.models.cliente_model import ClienteModel

class ClienteController:
    @staticmethod
    def adicionar_cliente(nome, email):
        cliente = ClienteModel(nome, email)
        cliente.salvar()

    @staticmethod
    def listar_clientes():
        return ClienteModel.listar_todos()

from app.models.venda_model import VendaModel

class VendaController:
    @staticmethod
    def adicionar_venda(cliente_id, produto_id, quantidade, data_venda, valor_total):
        venda = VendaModel(cliente_id, produto_id, quantidade, data_venda, valor_total)
        venda.salvar()

    @staticmethod
    def listar_vendas():
        return VendaModel.listar_todos()

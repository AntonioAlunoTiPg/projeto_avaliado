from app.models.produto_model import ProdutoModel

class ProdutoController:
    @staticmethod
    def adicionar_produto(nome, preco):
        produto = ProdutoModel(nome, preco)
        produto.salvar()

    @staticmethod
    def listar_produtos():
        return ProdutoModel.listar_todos()

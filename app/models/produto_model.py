from app.database.connection import conectar

class ProdutoModel:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    @staticmethod
    def listar_todos():
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM produtos")
        resultado = cursor.fetchall()
        conn.close()
        return resultado

    def salvar(self):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO produtos (nome, preco) VALUES (%s, %s)", (self.nome, self.preco))
        conn.commit()
        conn.close()

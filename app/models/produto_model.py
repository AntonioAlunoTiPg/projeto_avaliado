import mysql.connector
from mysql.connector import Error
from app.database.db_connection import get_connection

class ProdutoModel:
    def __init__(self):
        self.conn = get_connection()

    def listar_produtos(self):
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM produtos ORDER BY nome")
            return cursor.fetchall()
        except Error as e:
            print(f"Erro ao listar produtos: {e}")
            return []
        finally:
            cursor.close()

    def adicionar_produto(self, nome, preco):
        try:
            cursor = self.conn.cursor()
            sql = "INSERT INTO produtos (nome, preco) VALUES (%s, %s)"
            cursor.execute(sql, (nome, preco))
            self.conn.commit()
            return cursor.lastrowid
        except Error as e:
            print(f"Erro ao adicionar produto: {e}")
            return None
        finally:
            cursor.close()

    def excluir_produto(self, produto_id):
        try:
            cursor = self.conn.cursor()
            sql = "DELETE FROM produtos WHERE id = %s"
            cursor.execute(sql, (produto_id,))
            self.conn.commit()
            return cursor.rowcount
        except Error as e:
            print(f"Erro ao excluir produto: {e}")
            return None
        finally:
            cursor.close()

import mysql.connector
from mysql.connector import Error
from app.database.db_connection import get_connection

class VendaModel:
    def __init__(self):
        self.conn = get_connection()
    
    def registrar_venda(self, id_cliente, id_produto, quantidade, valor_total, data_venda=None):
        try:
            cursor = self.conn.cursor()
            query = """
                INSERT INTO vendas (id_cliente, id_produto, quantidade, valor_total, data_venda)
                VALUES (%s, %s, %s, %s, COALESCE(%s, NOW()))
            """
            cursor.execute(query, (id_cliente, id_produto, quantidade, valor_total, data_venda))
            self.conn.commit()
            return cursor.lastrowid
        except Error as e:
            print(f"Erro ao registrar venda: {e}")
            return None
        finally:
            cursor.close()

    def listar_vendas(self):
        try:
            cursor = self.conn.cursor(dictionary=True)
            query = """
                SELECT v.id, v.data_venda, c.nome AS cliente, p.nome AS produto, v.quantidade, v.valor_total
                FROM vendas v
                JOIN clientes c ON v.id_cliente = c.id
                JOIN produtos p ON v.id_produto = p.id
                ORDER BY v.data_venda DESC
            """
            cursor.execute(query)
            return cursor.fetchall()
        except Error as e:
            print(f"Erro ao listar vendas: {e}")
            return []
        finally:
            cursor.close()

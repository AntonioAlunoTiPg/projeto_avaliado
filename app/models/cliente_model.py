from app.database.db_connection import conectar

class ClienteModel:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    @staticmethod
    def listar_todos():
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM clientes")
        resultado = cursor.fetchall()
        conn.close()
        return resultado

    def salvar(self):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO clientes (nome, email) VALUES (%s, %s)", (self.nome, self.email))
        conn.commit()
        conn.close()

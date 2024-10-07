import mysql.connector
from mysql.connector import Error

class BancoDados:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='0000',
            database='escola'
        )
        self.cursor = self.conexao.cursor()

    def commit(self):
        self.conexao.commit()

    def close(self):
        self.conexao.close()

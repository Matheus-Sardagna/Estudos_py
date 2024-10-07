import mysql.connector
from mysql.connector import Error

class BancoDados:
    try:
        # Conectando ao banco de dados
        connection = mysql.connector.connect(
            host='localhost',         # Nome ou IP do servidor MySQL
            database='escola', # Nome do banco de dados
            user='root',           # Usuário do banco
            password='0000'          # Senha do banco
        )

        if connection.is_connected():
            db_info = connection.get_server_info()
            print("Conectado ao MySQL versão", db_info)
            cursor = connection.cursor()
            cursor.execute("SELECT DATABASE();")
            record = cursor.fetchone()
            print("Conectado ao banco de dados:", record)

    except Error as e:
        print("Erro ao conectar ao MySQL", e)

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("Conexão ao MySQL encerrada")

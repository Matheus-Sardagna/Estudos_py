from Escola import Escola
from BancoDados import BancoDados
class Turma():
    def __init__(self):
        self.escola = Escola()
        self.bd = BancoDados()
        self.cursor = self.bd.cursor

    def AdicionarTurma(self, nome, escola):
        sql = "INSERT INTO turma (nome, escola) VALUES (%s, %s)"
        self.cursor.execute(sql, (nome, escola.nome))
        self.bd.commit()

    def ListarTurmas(self):
        listar = "SELECT * FROM turma"
        self.cursor.execute(listar)
        return self.cursor.fetchall()

    def DeletarTurma(self, nome):
        sql = "DELETE FROM turma WHERE nome = %s"
        self.cursor.execute(sql, (nome,))
        self.bd.commit()
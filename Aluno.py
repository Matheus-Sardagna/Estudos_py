import CalcNota
from BancoDados import BancoDados

class Aluno:
    def __init__(self):
        self.bd = BancoDados()
        self.cursor = self.bd.cursor

    def AdicionarAluno(self, nome, nota1, nota2, nota3):
        calcMedia = CalcNota.CalcNota(nota1, nota2, nota3)
        media = calcMedia.media()
        situacao = self.situacao(media)

        sql = "INSERT INTO aluno (nome, media, situacao) VALUES (%s, %s, %s)"
        self.cursor.execute(sql, (nome, media, situacao))
        self.bd.commit()

    def ListarAlunos(self):
        listar = "SELECT * FROM aluno"
        self.cursor.execute(listar)
        return self.cursor.fetchall()

    def DeletarAluno(self, nome):
        sql = "DELETE FROM aluno WHERE nome = %s"
        self.cursor.execute(sql, (nome,))
        self.bd.commit()

    def situacao(self, media):
        if media >= 7:
            return "Aprovado"
        else:
            return "Reprovado"
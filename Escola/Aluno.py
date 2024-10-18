import CalcNota
from BancoDados import BancoDados
from Turma import Turma

class Aluno:
    def __init__(self):
        self.bd = BancoDados()
        self.cursor = self.bd.cursor
        self.turma = Turma()

    def AdicionarAluno(self, nome, nota1, nota2, nota3):
        calcMedia = CalcNota.CalcNota(nota1, nota2, nota3)
        media = calcMedia.media()
        situacao = self.situacao(media)

        sql = "INSERT INTO aluno (nome, media, situacao, turma) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(sql, (nome, media, situacao, self.turma.turma.nome))
        self.bd.commit()

    def ListarAlunos(self):
        listar = "SELECT * FROM aluno"
        self.cursor.execute(listar)
        return self.cursor.fetchall()

    def DeletarAluno(self, nome):
        sql = "DELETE FROM aluno WHERE nome = %s"
        self.cursor.execute(sql, (nome,))
        self.bd.commit()

    def AtualizarAluno(self,nome,media,situacao):
        sql = "UPDATE aluno SET media = %s, situacao = %s WHERE nome = %s"
        self.cursor.execute(sql, (media, situacao, nome))
        self.bd.commit()
    def situacao(self, media):
        if media >= 7:
            return "Aprovado"
        else:
            return "Reprovado"
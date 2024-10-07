import CalcNota
import BancoDados
class Aluno:
    cursor = BancoDados.cursor()
    def __init__(self,nome,media,situacao):
        self.nome = nome
        self.media = media
        self.situacao = situacao
    
    def AdicionarAluno(self, nota1, nota2, nota3):
        calcMedia = CalcNota.CalcNota(nota1, nota2, nota3)
        media = calcMedia.media()
        situacao = self.situacao(media)

        sql = "INSERT INTO alunos (nome, nota1, nota2, nota3, media, situacao) VALUES (%s, %s, %s, %s, %s, %s)"
        self.cursor.execute(sql, (self.nome, nota1, nota2, nota3, media, situacao))
        BancoDados.commit()
        
    def ListarAlunos(self):
        listar = "SELECT * FROM alunos"
        self.cursor.execute(listar)
        return self.cursor.fetchall()
        
    
    def DeletarAluno(self,nome):
        sql = "DELETE FROM alunos WHERE nome = %s"
        self.cursor.execute(sql, (nome,))
        BancoDados.commit() 

    def situacao(self,media):
        if media >= 7:
            return "Aprovado"
        else:
            return "Reprovado"
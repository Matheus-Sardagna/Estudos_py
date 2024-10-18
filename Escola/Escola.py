from BancoDados import BancoDados
class Escola:
    def __init__(self):
        self.bd = BancoDados()
        self.cursor = self.bd.cursor
    
    def adicionarEscola(self, nome):
        sql = "INSERT INTO escola (nome) VALUES (%s)"
        self.cursor.execute(sql, (nome,))
        self.bd.commit()

    def editarEscola(self, nome_antigo, nome_novo):
        sql = "UPDATE escola SET nome = %s WHERE nome = %s"
        self.cursor.execute(sql, (nome_novo, nome_antigo))
        self.bd.commit()
    
    def listarEscola(self):
        sql = "SELECT * FROM escola"
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    

    def deletarEscola(self, nome):
        sql = "DELETE FROM escola WHERE nome = %s"
        self.cursor.execute(sql, (nome,))
        self.bd.commit()

    
class CalcNota:
    def __init__(self, nota1, nota2, nota3):
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

    def media(self):
        media = (self.nota1 + self.nota2 + self.nota3) / 3
        if media > 10:
            media = 10
        return media
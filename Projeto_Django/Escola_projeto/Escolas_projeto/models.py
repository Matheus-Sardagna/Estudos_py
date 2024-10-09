from django.db import models

class Escola(models.Model):
    nome = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.nome
    
class Turma(models.Model):
    nome = models.CharField(max_length=100)
    escolaPertencente = models.ForeignKey(Escola, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.nome[:50]

# Create your models here.

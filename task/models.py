from django.db import models

# Create your models here.

class Task(models.Model):
    nome = models.CharField(max_length=25)
    descricao = models.CharField(max_length=244, null=True, blank=True)
    data_inicio = models.DateTimeField(null=True, blank=True)
    data_final = models.DateTimeField()
    
    def __str__(self):
        return self.nome
from django.db import models

# Create your models here.


class Curso(models.Model):

    Genero = (
        ("---", "---"),
        ("M", "Masculino"),
        ("F", "Feminino"),
        ("ND", "Não Definido"),
    )

  

    nome = models.CharField(max_length=255)
    rg = models.CharField(max_length=255)
    idade = models.CharField( max_length=255)
    cpf = models.CharField(max_length=255)
    sexo = models.CharField(choices=Genero, max_length=255)
    email = models.EmailField(max_length=255)
    telefone = models.CharField(max_length=255)    
    endereco = models.CharField(max_length=255)


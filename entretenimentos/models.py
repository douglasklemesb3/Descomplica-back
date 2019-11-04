from django.db import models

# Create your models here.
class Entretenimento(models.Model):

    Genero = (
        ("---", "---"),
        ("M", "Masculino"),
        ("F", "Feminino"),
        ("ND", "Não Definido"),
    )

    Periodo =(
        ("---","---"),
        ("M","Manha"),
        ("T","Tarde"),
        ("N","Noite"),
    )

    nome = models.CharField(max_length=255)
    rg = models.CharField(max_length=10)
    idade = models.IntegerField()
    dataNascimento = models.CharField(max_length=255)
    cpf = models.CharField(max_length=12)
    sexo = models.CharField(choices=Genero, max_length=255)
    email = models.EmailField(max_length=255)
    telefone = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    numero_de_recidencia = models.CharField(max_length=255)
    periodo = models.CharField(choices=Periodo,max_length=255)



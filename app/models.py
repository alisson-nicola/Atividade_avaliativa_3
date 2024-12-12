from django.db import models

class Funcionario(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    cpf = models.CharField(max_length=14, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    remuneracao = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)

    def __str__(self):
        return self.nome

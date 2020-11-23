from django.db import models


class Person(models.Model):
    edad = models.IntegerField()
    Nombre = models.CharField(max_length=100)
    Salario = models.IntegerField()

    def __str__(self):
        return self.Nombre

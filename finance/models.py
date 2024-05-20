from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=120, verbose_name='Nome', blank=False, null=False)
    doc = models.IntegerField(verbose_name='CPF', blank=False, null=False)
    income = models.FloatField(verbose_name='Renda', blank=False, null=False)

    def __str__(self):
        return f'Nome:{self.name}'



class Bill(models.Model):
    name = models.CharField(max_length=120, verbose_name='Nome', blank=False, null=False)
    price = models.FloatField(verbose_name='Valor', blank=False, null=False)
    due_date = models.DateField(verbose_name='Vencimento', blank=False, null=False)


    def __str__(self):
        return f'Nome:{self.name}'

from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

class Araba(models.Model):
    resim_linki = models.URLField()
    model = models.CharField(max_length=100)
    ilan_basli = models.CharField(max_length=100)
    km = models.IntegerField()
    fiyat = models.DecimalField(max_digits=8, decimal_places=2)
    
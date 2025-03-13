from django.db import models

class Drink(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)
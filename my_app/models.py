from django.db import models

# Create your models here.
class Person(models.Model):
    nick_name       = models.CharField(max_length=100, unique=True)
    first_name      = models.CharField(max_length=100)
    last_name       = models.CharField(max_length=100)
    address         = models.CharField(max_length=150)

    def __str__(self):
        return self.nick_name
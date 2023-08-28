from django.db import models

# Create your models here.

class Reja(models.Model):
    vaqt = models.CharField(max_length=100)
    text = models.CharField(max_length=200)
    status = models.CharField(max_length=200)

    def __str__(self):
        return self.vaqt
from django.db import models

# Create your models here.

class answers(models.Model):
    stage = models.CharField(max_length=200)
    answers=models.CharField(max_length=200)
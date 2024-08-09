from django.db import models

# Create your models here.

class car(models.Model):
  title = models.TextField(max_length=250)
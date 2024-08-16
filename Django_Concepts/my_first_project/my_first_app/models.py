from django.db import models

# Create your models here.

class Car(models.Model):
  title = models.TextField(max_length=250)
  year = models.TextField(max_length=4, null=True)
  color = models.TextField(max_length=20, default="White")

  def __str__(self) -> str:
    return f"{self.title} - {self.year}"
  
class Publisher (models.Model):
  name = models.TextField(max_length= 100)
  address = models.TextField(max_length= 100)

  def __str__(self) -> str:
    return f"{self.name} - {self.address}"
  
class Book (models.Model):
  title = models.TextField(max_length=100)
  publication_date = models.DateField()
  publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

  def __str__(self) -> str:
    return f"{self.title} - {self.publication_date}"
from django.db import models

# Create your models here.

class Juice(models.Model):
  name = models.CharField(max_length=30)
  price = models.CharField(max_length=10)
  description = models.CharField(max_length=80)

  def __str__(self):
    return f"name = {self.name}, price = {self.price}"

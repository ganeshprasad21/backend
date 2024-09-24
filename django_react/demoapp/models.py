from django.db import models

# Create your models here.

class Movie(models.Model):
  name = models.TextField()
  ratings = models.CharField(max_length=3)
  awards = models.TextField()
  year = models.BigIntegerField()

  def __str__(self):
    return f"name = {self.name} , year = {self.year}"

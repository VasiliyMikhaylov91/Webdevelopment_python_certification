from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=60, unique=True)
    description = models.TextField()
    sequence = models.TextField()
    cooking_time = models.IntegerField(validators=[MinValueValidator(1)])
    meal_image = models.ImageField()
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title
from django.db import models
from django.core.validators import MinValueValidator


# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=60, unique=True)
    description = models.TextField()
    sequence = models.TextField()
    cooking_time = models.IntegerField(validators=[MinValueValidator(1)])
    meal_image = models.ImageField()
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title

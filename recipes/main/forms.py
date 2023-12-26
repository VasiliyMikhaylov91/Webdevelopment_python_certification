from .models import Recipe
from django import forms


class RecipeForm(forms.Form):
    title = forms.CharField(max_length=60)
    description = forms.Textarea()
    sequence = forms.Textarea()
    cooking_time = forms.IntegerField(min_value=1)
    meal_image = forms.ImageField()
    author = forms.CharField(max_length=100)
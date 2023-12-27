from .models import Recipe
from django import forms


class RecipeForm(forms.Form):
    title = forms.CharField(max_length=60)
    description = forms.CharField(max_length=1_000_000)
    sequence = forms.CharField(max_length=1_000_000)
    cooking_time = forms.IntegerField(min_value=1)
    meal_image = forms.ImageField()
    author = forms.CharField(max_length=100)


class ImgForm(forms.Form):
    meal_image = forms.ImageField()


class DescriptionForm(forms.Form):
    description = forms.CharField(max_length=1_000_000)


class SequenceForm(forms.Form):
    sequence = forms.CharField(max_length=1_000_000)


class CookingTimeForm(forms.Form):
    cooking_time = forms.IntegerField(min_value=1)
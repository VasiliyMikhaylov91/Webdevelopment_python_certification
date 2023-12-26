from .models import Recipe
from django.forms import ModelForm, TextInput, Textarea, NumberInput, FileInput


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ["title", "description", "sequence", "cooking_time", "meal_image", "author"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
            "sequence": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите последовательность приготовления'
            }),
            "cooking_time": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Время приготовления, мин'
            }),
            "meal_image": FileInput(attrs={
                'class': 'form-control',
            }),
            "author": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите автора'
            }),
        }

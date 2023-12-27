from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Recipe
from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Логин', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class RecipeForm(forms.Form):
    title = forms.CharField(max_length=60, label='Название', widget=forms.TextInput(attrs={'class': 'form-input'}))
    description = forms.CharField(max_length=1_000_000, label='Описание',
                                  widget=forms.Textarea(attrs={'class': 'form-input'}))
    sequence = forms.CharField(max_length=1_000_000, label='Шаги приготовления',
                               widget=forms.Textarea(attrs={'class': 'form-input'}))
    cooking_time = forms.IntegerField(min_value=1, label='Врема приготовления, мин',
                                      widget=forms.TextInput(attrs={'class': 'form-input'}))
    meal_image = forms.ImageField(label='Изображение')
    author = forms.CharField(max_length=100, label='Автор', widget=forms.TextInput(attrs={'class': 'form-input'}))

    class Meta:
        model = Recipe
        fields = ('title', 'description', 'sequence', 'cooking_time', 'meal_image', 'author')


class ImgForm(forms.Form):
    meal_image = forms.ImageField(label='Изображение')

    class Meta:
        model = Recipe
        fields = 'meal_image'


class DescriptionForm(forms.Form):
    description = forms.CharField(max_length=1_000_000)

    class Meta:
        model = Recipe
        fields = 'description'


class SequenceForm(forms.Form):
    sequence = forms.CharField(max_length=1_000_000)

    class Meta:
        model = Recipe
        fields = 'sequence'


class CookingTimeForm(forms.Form):
    cooking_time = forms.IntegerField(min_value=1)

    class Meta:
        model = Recipe
        fields = 'cooking_time'

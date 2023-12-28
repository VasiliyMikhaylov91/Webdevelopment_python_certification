from django.contrib.auth import get_user_model
from .models import Recipe
from django import forms

User = get_user_model()


class LoginForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ['username', 'password']

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = User.objects.filter(username=username).first()
        if not user:
            raise forms.ValidationError(f'Пользователь с логином {username} не зарегестрирован')
        if not user.check_password(password):
            raise forms.ValidationError(f'Неверный пароль')
        return self.cleaned_data


class RegisterForm(forms.ModelForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Электронная почта', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password_confirm = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password_confirm')

    def clean(self):
        username = self.cleaned_data['username']
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        password_confirm = self.cleaned_data['password_confirm']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(f'Пользователь с именем {username} уже зарегестрирован')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(f'Электронная почта {email} используется другим пользователем')
        if password != password_confirm:
            raise forms.ValidationError('Пароли не совпадают')
        return self.cleaned_data


class RecipeForm(forms.Form):
    title = forms.CharField(max_length=60, label='Название', widget=forms.TextInput(attrs={'class': 'form-input'}))
    description = forms.CharField(max_length=1_000_000, label='Описание',
                                  widget=forms.Textarea(attrs={'class': 'form-input'}))
    sequence = forms.CharField(max_length=1_000_000, label='Шаги приготовления',
                               widget=forms.Textarea(attrs={'class': 'form-input'}))
    cooking_time = forms.IntegerField(min_value=1, label='Врема приготовления, мин',
                                      widget=forms.NumberInput(attrs={'class': 'form-input'}))
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

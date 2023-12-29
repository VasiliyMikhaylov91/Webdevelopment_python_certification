from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from random import choice

from .models import Recipe
from .forms import RegisterForm, LoginForm, User, RecipeForm, ImgForm, DescriptionForm, SequenceForm, CookingTimeForm


# Create your views here.
def index(request):
    positions = Recipe.objects.all()
    recipes_list = None
    if positions:
        recipes_list = []
        for _ in range(4):
            recipes_list.append(choice(positions))
    return render(request, 'main/index.html', {'recipes': recipes_list})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User(username=username, email=email, password=password)
            user.save()
            request.session['username'] = user.username
            return redirect('home')
    form = RegisterForm()
    context = {'title': 'Регистрация пользователя', 'form': form}
    return render(request, 'main/user.html', context)


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = User.objects.filter(username=form.cleaned_data['username']).first()
            request.session['username'] = user.username
            return redirect('home')
    form = LoginForm()
    context = {'title': 'Вход', 'form': form}
    return render(request, 'main/user.html', context)


def logout(request):
    del request.session
    return redirect('/')


def recipes(request):
    positions = Recipe.objects.all()
    return render(request, 'main/recipes.html', {'positions': positions})


def recipe_page(request, pk):
    position = Recipe.objects.filter(id=pk).first()
    context = {
        "pk": pk,
        "title": position.title,
        "description": position.description,
        "sequence": position.sequence,
        "cooking_time": position.cooking_time,
        "meal_image": position.meal_image,
        "author": position.author
    }
    return render(request, 'main/recipe_page.html', context)


def change_img(request, pk):
    position = Recipe.objects.filter(id=pk).first()
    if request.method == 'POST':
        form = ImgForm(request.POST, request.FILES)
        if form.is_valid():
            meal_image = form.cleaned_data['meal_image']
            position.meal_image = meal_image
            position.save()
            fs = FileSystemStorage()
            fs.save(meal_image.name, meal_image)
            return redirect(f'/recipes/{pk}')
    form = ImgForm()
    context = {'action': f'Изменить изображение для {position.title}', 'form': form}
    return render(request, 'main/recipe_conf.html', context)


def change_description(request, pk):
    position = Recipe.objects.filter(id=pk).first()
    if request.method == 'POST':
        form = DescriptionForm(request.POST)
        if form.is_valid():
            description = form.cleaned_data['description']
            position.description = description
            position.save()
            return redirect(f'/recipes/{pk}')
    form = DescriptionForm()
    context = {'action': f'Изменить описание для {position.title}', 'form': form}
    return render(request, 'main/recipe_conf.html', context)


def change_sequence(request, pk):
    position = Recipe.objects.filter(id=pk).first()
    if request.method == 'POST':
        form = SequenceForm(request.POST)
        if form.is_valid():
            sequence = form.cleaned_data['sequence']
            position.sequence = sequence
            position.save()
            return redirect(f'/recipes/{pk}')
    form = SequenceForm()
    context = {'action': f'Изменить шаги приготовления для {position.title}', 'form': form}
    return render(request, 'main/recipe_conf.html', context)


def change_cooking_time(request, pk):
    position = Recipe.objects.filter(id=pk).first()
    if request.method == 'POST':
        form = CookingTimeForm(request.POST)
        if form.is_valid():
            cooking_time = form.cleaned_data['cooking_time']
            position.cooking_time = cooking_time
            position.save()
            return redirect(f'/recipes/{pk}')
    form = CookingTimeForm()
    context = {'action': f'Изменить время приготовления для {position.title}', 'form': form}
    return render(request, 'main/recipe_conf.html', context)


def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            sequence = form.cleaned_data['sequence']
            cooking_time = form.cleaned_data['cooking_time']
            meal_image = form.cleaned_data['meal_image']
            author = form.cleaned_data['author']
            fs = FileSystemStorage()
            fs.save(meal_image.name, meal_image)
            recipe = Recipe(title=title, description=description, sequence=sequence, cooking_time=cooking_time,
                            meal_image=meal_image, author=author)
            recipe.save()
            return redirect('recipes')
    else:
        form = RecipeForm()
    context = {'action': 'Добавить рецепт', 'form': form}
    return render(request, 'main/recipe_conf.html', context)


def info(request):
    return render(request, 'main/info.html')

from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from random import choice
from django.http import JsonResponse

from .models import Recipe
from .forms import RegisterForm, LoginForm, User, RecipeForm, ImgForm, DescriptionForm, SequenceForm, CookingTimeForm


# Create your views here.


def head(func):
    def wrapper(request, *args, **kwargs):
        username = None
        if '_auth_user_id' in request.session:
            username = request.session['username']
        # kwargs['username'] = username
        return func(request, *args, **kwargs)

    return wrapper


@head
def index(request, **kwargs):
    positions = Recipe.objects.all()
    recipes_list = None
    if positions:
        recipes_list = []
        for _ in range(4):
            recipes_list.append(choice(positions))
    context = {'recipes': recipes_list}
    return render(request, 'main/index.html', context | kwargs)


@head
def register(request, **kwargs):
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
    context = {'title': 'Регистрация пользователя', 'form': form, 'action': 'Зарегестрароваться'}
    return render(request, 'main/user.html', context | kwargs)


@head
def login(request, **kwargs):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = User.objects.filter(username=form.cleaned_data['username']).first()
            request.session['username'] = user.username
            return redirect('home')
    form = LoginForm()
    context = {'title': 'Вход', 'form': form, 'action': 'Войти'}
    return render(request, 'main/user.html', context | kwargs)


def logout(request):
    del request.session['username']
    return redirect('/')


@head
def recipes(request, **kwargs):
    positions = Recipe.objects.all()
    context = {'positions': positions}
    return render(request, 'main/recipes.html', context | kwargs)


@head
def recipe_page(request, pk, **kwargs):
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
    return render(request, 'main/recipe_page.html', context | kwargs)


@head
def change_img(request, pk, **kwargs):
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
    return render(request, 'main/recipe_conf.html', context | kwargs)


@head
def change_description(request, pk, **kwargs):
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
    return render(request, 'main/recipe_conf.html', context | kwargs)


@head
def change_sequence(request, pk, **kwargs):
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
    return render(request, 'main/recipe_conf.html', context | kwargs)


@head
def change_cooking_time(request, pk, **kwargs):
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
    return render(request, 'main/recipe_conf.html', context | kwargs)


@head
def add_recipe(request, **kwargs):
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
    return render(request, 'main/recipe_conf.html', context | kwargs)


@head
def info(request, **kwargs):
    context = dict()
    return render(request, 'main/info.html', context | kwargs)


def test(request):
    return JsonResponse(dict(request.session), json_dumps_params={'ensure_ascii': False})

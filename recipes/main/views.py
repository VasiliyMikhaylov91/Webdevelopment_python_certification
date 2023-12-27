import os

from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

from .models import User, Recipe
from .forms import RecipeForm, ImgForm


# Create your views here.
def index(request):
    return render(request, 'main/index.html')


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
            #os.remove(f'/media/{position.meal_image}')
            position.meal_image = meal_image
            position.save()
            fs = FileSystemStorage()
            fs.save(meal_image.name, meal_image)
            return redirect(f'/recipes/{pk}')
    form = ImgForm()
    context = {'action': f'Изменить изображение для {position.title}', 'form': form}
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

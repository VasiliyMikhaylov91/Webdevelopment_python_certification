from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

from .models import User, Recipe
from .forms import RecipeForm


# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def recipes(request):
    positions = Recipe.objects.all()
    return render(request, 'main/recipes.html', {'positions': positions})


def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
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
    else:
        form = RecipeForm()
    context = {'action': 'Добавить', 'form': form}
    return render(request, 'main/recipe_conf.html', context)

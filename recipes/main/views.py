from django.shortcuts import render, redirect
from .models import User, Recipe
from .forms import RecipeForm


# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def recipes(request):
    positions = Recipe.objects.all()
    return render(request, 'main/recipes.html', {'positions': positions})


def add_recipe(request):
    error = ''
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recipes')
        else:
            error = 'Форма заполнена неверно'
    form = RecipeForm()
    context = {'action': 'Создать', 'form': form, 'error': error}
    return render(request, 'main/recipe_conf.html', context)

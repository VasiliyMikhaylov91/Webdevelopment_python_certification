from django.urls import path
from .views import index, recipes, add_recipe

urlpatterns = [
    path('', index, name='home'),
    path('recipes', recipes, name='recipes'),
    path('new_recipe', add_recipe, name='add_recipe')
]
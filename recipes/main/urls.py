from django.urls import path
from .views import index, recipes, add_recipe, recipe_page

urlpatterns = [
    path('', index, name='home'),
    path('recipes/<int:pk>', recipe_page),
    path('recipes/', recipes, name='recipes'),
    path('new_recipe/', add_recipe, name='add_recipe'),
]
from django.urls import path
from .views import index, recipes, add_recipe, recipe_page, change_img, change_description, change_sequence, \
    change_cooking_time

urlpatterns = [
    path('', index, name='home'),
    path('recipes/<int:pk>/change_img/', change_img),
    path('recipes/<int:pk>/change_description/', change_description),
    path('recipes/<int:pk>/change_sequence/', change_sequence),
    path('recipes/<int:pk>/change_cooking_time/', change_cooking_time),
    path('recipes/<int:pk>/', recipe_page),
    path('recipes/', recipes, name='recipes'),
    path('new_recipe/', add_recipe, name='add_recipe'),
]

from django.urls import path, include
from .views import index, register, login, logout, info, recipes, add_recipe, recipe_page, change_img, \
    change_description, change_sequence, change_cooking_time, test

urlpatterns = [
    path('', index, name='home'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('recipes/<int:pk>/change_img/', change_img),
    path('recipes/<int:pk>/change_description/', change_description),
    path('recipes/<int:pk>/change_sequence/', change_sequence),
    path('recipes/<int:pk>/change_cooking_time/', change_cooking_time),
    path('recipes/<int:pk>/', recipe_page),
    path('recipes/', recipes, name='recipes'),
    path('new_recipe/', add_recipe, name='add_recipe'),
    path('info/', info, name='info'),
    path('test/', test, name='test'),
    path('accounts/', include('django.contrib.auth.urls'))
]

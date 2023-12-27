from django.contrib import admin
from .models import Recipe, User

# Register your models here.
admin.site.register(User)
admin.site.register(Recipe)
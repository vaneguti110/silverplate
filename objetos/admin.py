from django.contrib import admin
from .models import Ingredient, User, Image, Recipe, Comment
# Register your models here.

admin.site.register(Ingredient)

admin.site.register(User)

admin.site.register(Image)

admin.site.register(Recipe)

admin.site.register(Comment)
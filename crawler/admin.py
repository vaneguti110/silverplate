from django.contrib import admin

from .models import IngredientSpec


@admin.register(IngredientSpec)
class IngredientSpecAdmin(admin.ModelAdmin):
    pass

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView

from .models import IngredientSpec, IgnoredWords
from objetos.models import Ingredient


# Create your views here.
class IngredientSpecList(ListView):
    context_object_name = 'ingredients'
    ordering = '-count'
    model = IngredientSpec
    paginate_by = 20


def salvar_palavra_ignorar(request):
    if request.method == 'POST':
        word = request.POST.get('word')
        word = word.strip()
        if not ignore_word_exists(word):
            update_spec(word)
            Ignorar = IgnoredWords(Word=word)
            Ignorar.save()

            Ingredients = Ingredient.objects.all()
            for ing in Ingredients:
                clear_specs(ing.description)

    return HttpResponseRedirect('/crawl')


def delete_spec(request):
    if request.method == 'POST':
        spec_id = request.POST.get('id')
        word = request.POST.get('word')
        spec = IngredientSpec(id=spec_id, word=word)
        spec.delete()

    return HttpResponseRedirect('/crawl')


def salvar_Ingrediente(request):
    if request.method == 'POST':
        new_ingredient = request.POST.get('word')
        ing = Ingredient(description=new_ingredient.title())
        ing.save()

        clear_specs(new_ingredient)
    return HttpResponseRedirect('/crawl')


def update_spec(pal_ignorar):
    list_ingredients = IngredientSpec.objects.order_by('-Count')
    for Ingredient in list_ingredients:
        Ingredient.Word = Ingredient.Word.replace(pal_ignorar, '').strip()
        print(Ingredient)
        Ingredient.save()


def ignore_word_exists(word):
    return IgnoredWords.objects.filter(word=word).exists()


def clear_specs(new_ingredient):
    try:
        print(new_ingredient.title())
        delete_list = IngredientSpec.objects.filter(word=new_ingredient.lower())
        for spec in delete_list:
            spec.delete()
    except IngredientSpec.DoesNotExist:
        print('sem chance')

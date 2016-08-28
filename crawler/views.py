from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import IngredientSpec, IgnoredWords
from objetos.models import Ingredient


# Create your views here.
def index(request):
    ingredients = IngredientSpec.objects.order_by('-count')[:20]
    return render(request, 'crawler/index.html', {'ingredients': ingredients})


def salvar_palavra_ignorar(request):
    if request.method == 'POST':
        word = request.POST.get('word')
        word = word.strip()
        if not exists_palavra_ignorar(word):
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


def exists_palavra_ignorar(word):
    try:
        existe_palavra = IgnoredWords.objects.get(word=word)
        return 1
    except IgnoredWords.DoesNotExist:
        return 0


def clear_specs(new_ingredient):
    try:
        print(new_ingredient.title())
        delete_list = IngredientSpec.objects.filter(word=new_ingredient.lower())
        for spec in delete_list:
            spec.delete()
    except IngredientSpec.DoesNotExist:
        print('sem chance')

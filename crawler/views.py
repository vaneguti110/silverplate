from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Ingredient_Spec, Palavras_Ignorar
from objetos.models import Ingredient

# Create your views here.
def index(request):
	lista = Ingredient_Spec.objects.order_by('-Count')[:20]
	return render(request,'index.html',{'lista':lista})

def salvar_palavra_ignorar(request):
	if request.method == 'POST':
		word = request.POST.get('word')
		word = word.strip()
		if not exists_palavra_ignorar(word):
			atualizar_spec(word)
			Ignorar = Palavras_Ignorar(Palavra=word)
			Ignorar.save()

			Ingredients = Ingredient.objects.all()
			for ing in Ingredients:
				limpeza_specs(ing.descricao)

	return HttpResponseRedirect('/crawl')

def salvar_Ingrediente(request):
	if request.method == 'POST':
		novo_Ingredient = request.POST.get('word')
		ing = Ingredient(descricao = novo_Ingredient.title())
		ing.save()

		limpeza_specs(novo_Ingredient)
	return HttpResponseRedirect('/crawl')

def atualizar_spec(pal_ignorar):
	lista = Ingredient_Spec.objects.order_by('-Count')
	for Ingredient in lista:
		Ingredient.Palavra = Ingredient.Palavra.replace(pal_ignorar, '').strip()
		Ingredient.save()


def exists_palavra_ignorar(palavra):
	try:
		existe_palavra = Palavras_Ignorar.objects.get(Palavra=palavra)
		return 1
	except Palavras_Ignorar.DoesNotExist:
		return 0

def limpeza_specs(novo_Ingredient):
	try:
		print(novo_Ingredient.title())
		lista_excluir = Ingredient_Spec.objects.filter(Palavra=novo_Ingredient.lower())
		for spec in lista_excluir:
			spec.delete()
	except Ingredient_Spec.DoesNotExist:
		print('sem chance')
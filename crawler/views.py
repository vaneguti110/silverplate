from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Ingrediente_Spec, Palavras_Ignorar
from objetos.models import Ingrediente

# Create your views here.
def index(request):
	lista = Ingrediente_Spec.objects.order_by('-Count')[:20]
	return render(request,'index.html',{'lista':lista})

def salvar_palavra_ignorar(request):
	if request.method == 'POST':
		word = request.POST.get('word')
		word = word.strip()
		if not exists_palavra_ignorar(word):
			atualizar_spec(word)
			Ignorar = Palavras_Ignorar(Palavra=word)
			Ignorar.save()

			ingredientes = Ingrediente.objects.all()
			for ing in ingredientes:
				limpeza_specs(ing.descricao)

	return HttpResponseRedirect('/crawl')

def salvar_ingrediente(request):
	if request.method == 'POST':
		novo_ingrediente = request.POST.get('word')
		ing = Ingrediente(descricao = novo_ingrediente.title())
		ing.save()

		limpeza_specs(novo_ingrediente)
	return HttpResponseRedirect('/crawl')

def atualizar_spec(pal_ignorar):
	lista = Ingrediente_Spec.objects.order_by('-Count')
	for ingrediente in lista:
		ingrediente.Palavra = ingrediente.Palavra.replace(pal_ignorar, '').strip()
		ingrediente.save()


def exists_palavra_ignorar(palavra):
	try:
		existe_palavra = Palavras_Ignorar.objects.get(Palavra=palavra)
		return 1
	except Palavras_Ignorar.DoesNotExist:
		return 0

def limpeza_specs(novo_ingrediente):
	try:
		print(novo_ingrediente.title())
		lista_excluir = Ingrediente_Spec.objects.filter(Palavra=novo_ingrediente.lower())
		for spec in lista_excluir:
			spec.delete()
	except Ingrediente_Spec.DoesNotExist:
		print('sem chance')
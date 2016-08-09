from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Ingrediente_Spec

# Create your views here.
def index(request):
	lista = Ingrediente_Spec.objects.order_by('-Count')
	return render(request,'index.html',{'lista':lista})
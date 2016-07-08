from django.contrib import admin
from .models import Ingrediente, Usuario, Imagem, Receita, Comentario
# Register your models here.

admin.site.register(Ingrediente)

admin.site.register(Usuario)

admin.site.register(Imagem)

admin.site.register(Receita)

admin.site.register(Comentario)
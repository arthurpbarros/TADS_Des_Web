from django.contrib import admin
from .models import *

class RespostaInline(admin.TabularInline):
    model = Resposta
    extra = 2

class QuestaoInline(admin.TabularInline):
    model = Questao
    extra = 0

class QuestaoAdmin(admin.ModelAdmin):
    list_display = ['texto']
    list_filter = ['simulado']
    inlines = [RespostaInline]

class SimuladoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor']
    list_filter = ['autor']
    inlines = [QuestaoInline]

admin.site.register(Simulado,SimuladoAdmin)
# Register your models here.
admin.site.register(Questao,QuestaoAdmin)

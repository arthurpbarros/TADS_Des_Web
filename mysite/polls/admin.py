'''
from django.contrib import admin
from .models import *  #Choice, Question

# Register your models here.
admin.site.register(Choice)
admin.site.register(Question)
'''
from django.contrib import admin
from .models import Question, Choice, Rotulo, Autor, Perfil

admin.AdminSite.site_header = 'Administração da Aplicação de Enquetes'
### Definição do Formulário para as Perguntas
#############################################
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['autor', 'question_text', 'rotulos']}),
        ('Informações de Data', {'fields': ['pub_date', 'end_date']})
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'id', 'autor', 'pub_date', 'publicada_recentemente')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)


### Definição do Formulário para os Rótulos
###########################################
class RotuloAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'id')

admin.site.register(Rotulo, RotuloAdmin)


### Definição do Formulário para os Autores
###########################################
class PerfilInline(admin.StackedInline):
    model = Perfil

class AutorAdmin(admin.ModelAdmin):
    inlines = [PerfilInline]
    list_display = ('nome', 'id')

admin.site.register(Autor, AutorAdmin)
### Registrando os módulos seguintes


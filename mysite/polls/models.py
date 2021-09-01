import datetime
from django.db import models
from django.utils import timezone


###     Clase Autor
##########################
class Autor(models.Model):
    nome = models.CharField(max_length=80)

    class Meta:
        ordering = ['nome']
        verbose_name_plural = 'Autores'
    def __str__(self):
        return self.nome

###     Classe Perfil
###########################
class Perfil(models.Model):
    descricao = models.TextField()
    cidade = models.CharField(max_length=50)
    pais = models.CharField(max_length=30)
    genero = models.CharField(max_length=100)
    autor = models.OneToOneField(Autor, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Informações de Perfil'
    def __str__(self):
        return self.autor.nome

###     Classe Rotulo
###########################
class Rotulo(models.Model):
    titulo = models.CharField(max_length=30)

    class Meta:
        ordering = ['titulo']
        verbose_name = 'Rótulo'
        verbose_name_plural = 'Rótulos'
    def __str__(self):
        return self.titulo

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Data de publicação')
    end_date = models.DateField('Data de Encerramento', null=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, null=True)
    rotulos = models.ManyToManyField(Rotulo, verbose_name='Rótulos')

    def __str__ (self):
        return self.question_text

    def publicada_recentemente(self):
	    date_now = timezone.now()
	    return date_now-datetime.timedelta(days=1)<=self.pub_date<=date_now
    publicada_recentemente.admin_order_field = 'data_publicacao'
    publicada_recentemente.boolean = True
    publicada_recentemente.short_description = 'É recente?'


class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    class Meta:
        ordering = ['choice_text']
        verbose_name = 'Opção'
        verbose_name_plural = 'Opções'
    def __str__ (self):
        return self.choice_text

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Simulado(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    autor = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name_plural = "simulados"

class Questao(models.Model):
    texto = models.TextField()
    pontuacao = models.PositiveIntegerField(default=0)
    simulado = models.ForeignKey('Simulado',on_delete=models.CASCADE)

    def __str__(self):
        return self.texto

    def get_respostas(self):
        return Resposta.objects.filter(questao=self)

    class Meta:
        verbose_name_plural = "questões"

class Resposta(models.Model):
    texto = models.CharField(max_length=200)
    questao = models.ForeignKey('Questao',on_delete=models.CASCADE)
    correta = models.BooleanField(default=False)

    def __str__(self):
        return self.texto

    class Meta:
        verbose_name_plural = "respostas"

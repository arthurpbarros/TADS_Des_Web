from django.db import models

# Create your models here.
class Simulado(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=200,blank=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    text = models.TextField()
    score = models.PositiveIntegerField(default=1)
    simulado = models.ForeignKey(Simulado,on_delete=models.CASCADE)

    def __str__(self):
        return self.text + ' (' + self.score + ')'

class Choice(models.Model):
    value = models.CharField(max_length=150)
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)

    def __str__(self):
        return self.value + ' (' + self.is_correct + ')'



from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('Data de publicação')

	def __str__ (self):
	    return self.question_text

	def is_last(self):
	    date_now = timezone.now()
	    return date_now-datetime.timedelta(days=1)<=self.pub_date<=date_now

class Choice(models.Model):
	question = models.ForeignKey(Question,on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__ (self):
	    return self.choice_text

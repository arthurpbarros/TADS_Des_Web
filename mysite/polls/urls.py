from django.urls import path
from . import views


app_name = 'polls'
urlpatterns = [
	path('', views.index, name='index'),
	path('details/<int:question_id>/',views.details,name='details'),
	path('result/<int:question_id>/',views.result,name='result'),
	path('vote/<int:question_id>/',views.vote,name='vote')
	#path('all/',views.viewQuestions,name='all')
]

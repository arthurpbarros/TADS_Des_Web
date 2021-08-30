from django.shortcuts import render,get_object_or_404,render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from polls.models import Question, Choice
#from django.views import generic

# Create your views here.
def index(request):
    last_questions = Question.objects.filter(pub_date__lte = timezone.now()).order_by('-pub_date')
    return render(request,'polls/index.html', {'questions': last_questions})

def details(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/details.html', {'question':question})

def vote(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        select_choice = question.choice_set.get(pk=request.POST['option'])
    except (KeyError, Choice.DoesNotExist):
        return render(request,'polls/details.html',{'question': question,
        'message': 'Você não selecionou nenhuma opção!'})
    else:
        select_choice.votes = select_choice.votes + 1
        select_choice.save()
        return HttpResponseRedirect(reverse('polls:result', args=[question_id]))

def result(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/result.html',{'question': question})

# def viewQuestions(request):
#    result = Question.objects.all()
#    return render_to_response('polls/viewQuestions.html', {'questions': result})


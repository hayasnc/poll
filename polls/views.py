from django.http import HttpResponse
from .models import Question
from django.shortcuts import render, get_object_or_404
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

# def details(request, question_id):
#     try:
#         q = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Questions does't exist")
#     return render(request, 'polls/details.html', {'question': q})

def details(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/details.html', {'question': q})

def result(request, question_id):
    response = "You're looking at the results of question %s"
    return HttpResponse(response %question_id)

def voting(request, question_id):
    return HttpResponse("Voting for Question %s" %question_id)

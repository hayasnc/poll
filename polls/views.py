from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def details(request, question_id):
    return HttpResponse("You're viewing Question with id %s" %question_id)

def result(request, question_id):
    response = "You're looking at the results of question %s"
    return HttpResponse(response %question_id)

def voting(request, question_id):
    return HttpResponse("Voting for Question %s" %question_id)

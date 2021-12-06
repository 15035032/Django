from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, response


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    return HttpResponse("You are looking at questions %s." % question_id)

def results(request, question_id):
    response = "You are looking at the result of the question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return("You're voting on question %s." % question_id)
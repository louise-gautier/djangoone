from django.shortcuts import render
from django.http import HttpResponse


# C'est ici qu'on run les calculs python pour préparer les pages html
# C'est l'équivalent de routes en flask environ


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def index2(request):
    dicos = [{'name': 'd1'}, {'name': 'd2'}, {'name': 'd3'}]
    context = {'dicos': dicos}
    print(context)
    return render(request, 'polls/index.html', context)

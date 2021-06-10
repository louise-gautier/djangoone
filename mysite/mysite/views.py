from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("MySITE/VIEWS.PY:DEF INDEX - Bienvenu(e)s à la racine de mon projet de test pour apprendre les rouages de Django.")



from django.urls import path

from . import views

# Centralisation des def de views avec attribution de l'url
# C'est l'equivalent des décorateurs dans routes en Flask

urlpatterns = [
    path('', views.index, name='index'),
    path('2/', views.index2, name='index2'),
]

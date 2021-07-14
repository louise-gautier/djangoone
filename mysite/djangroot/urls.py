from django.urls import path

from . import views

# Centralisation des def de views avec attribution de l'url
# C'est l'equivalent des décorateurs dans routes en Flask

app_name = 'djangroot_name'
urlpatterns = [
    #path('', views.index, name='index'),
    #path('2/', views.index2, name='index2'),
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name="logout"),
]


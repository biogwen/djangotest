from django.urls import path
from . import views

urlpatterns = [
    path('', views.form, name='formulaire'),
    path('rendu/', views.rendu, name='rendu_information'),

]
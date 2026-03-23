from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('rendezvous/', views.ajouter_rdv, name='ajouter_rdv'),
    path('liste/', views.liste_rdv, name='liste_rdv'),
    path('supprimer/<int:id>/', views.supprimer_rdv, name='supprimer_rdv'),
]
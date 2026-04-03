from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('rendezvous/', views.prendre_rendezvous, name='prendre_rendezvous'),
    path('confirmation/', views.confirmation, name='confirmation'),
    path('liste/', views.liste_rdv, name='liste_rdv'),
    path('modifier/<int:id>/', views.modifier_rdv, name='modifier_rdv'),
    path('supprimer/<int:id>/', views.supprimer_rdv, name='supprimer_rdv'),
]
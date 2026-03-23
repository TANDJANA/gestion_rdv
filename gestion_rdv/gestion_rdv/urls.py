from django.contrib import admin
from django.urls import path
from rdv import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.accueil, name='accueil'),
    path('rendezvous/', views.ajouter_rdv, name='ajouter_rdv'),
    path('rendezvous/liste/', views.liste_rdv, name='liste_rdv'),
    path('rendezvous/modifier/<int:id>/', views.modifier_rdv, name='modifier_rdv'),
    path('rendezvous/supprimer/<int:id>/', views.supprimer_rdv, name='supprimer_rdv'),

    # AUTH
    path('login/', auth_views.LoginView.as_view(template_name='rdv/login.html'), name='login'),
    path('logout/', views.deconnexion, name='logout'),
]
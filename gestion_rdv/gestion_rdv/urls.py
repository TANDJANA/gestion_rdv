from django.contrib import admin
from django.urls import path
from rdv import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Accueil
    path('', views.accueil, name='accueil'),

    # PATIENT (sans login)
    path('rendezvous/', views.prendre_rdv, name='prendre_rdv'),

    # ADMIN (avec login)
    path('dashboard/', views.dashboard, name='dashboard'),
    path('rdv/liste/', views.liste_rdv, name='liste_rdv'),
    path('rdv/modifier/<int:id>/', views.modifier_rdv, name='modifier_rdv'),
    path('rdv/supprimer/<int:id>/', views.supprimer_rdv, name='supprimer_rdv'),

    # AUTH
    path('login/', auth_views.LoginView.as_view(template_name='rdv/login.html'), name='login'),
    path('logout/', views.deconnexion, name='logout'),
]
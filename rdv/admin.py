from django.contrib import admin
from .models import Hopital, Medecin, RendezVous

admin.site.register(Hopital)
admin.site.register(Medecin)
admin.site.register(RendezVous)
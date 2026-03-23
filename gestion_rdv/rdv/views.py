from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import RendezVous, Medecin


@login_required
def accueil(request):
    return render(request, 'rdv/accueil.html')


@login_required
def ajouter_rdv(request):
    medecins = Medecin.objects.all()

    if request.method == "POST":
        patient = request.POST.get("patient")
        date = request.POST.get("date")
        heure = request.POST.get("heure")
        medecin_id = request.POST.get("medecin")

        medecin = Medecin.objects.get(id=medecin_id)

        RendezVous.objects.create(
            patient=patient,
            date=date,
            heure=heure,
            medecin=medecin
        )

        return redirect('liste_rdv')

    return render(request, 'rdv/rendezvous.html', {'medecins': medecins})


@login_required
def liste_rdv(request):
    rdvs = RendezVous.objects.all()
    return render(request, 'rdv/liste.html', {'rdvs': rdvs})


@login_required
def modifier_rdv(request, id):
    rdv = get_object_or_404(RendezVous, id=id)
    medecins = Medecin.objects.all()

    if request.method == "POST":
        rdv.patient = request.POST.get("patient")
        rdv.date = request.POST.get("date")
        rdv.heure = request.POST.get("heure")
        medecin_id = request.POST.get("medecin")
        rdv.medecin = Medecin.objects.get(id=medecin_id)

        rdv.save()
        return redirect('liste_rdv')

    return render(request, 'rdv/modifier.html', {'rdv': rdv, 'medecins': medecins})


@login_required
def supprimer_rdv(request, id):
    rdv = get_object_or_404(RendezVous, id=id)
    rdv.delete()
    return redirect('liste_rdv')

from django.contrib.auth import logout

def deconnexion(request):
    logout(request)
    return redirect('login')


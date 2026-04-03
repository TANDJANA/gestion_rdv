from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import RendezVous, Medecin


def accueil(request):
    return render(request, 'rdv/accueil.html')


# ================== PATIENT ==================
def prendre_rdv(request):
    medecins = Medecin.objects.all()

    if request.method == "POST":
        patient = request.POST.get("patient")
        date = request.POST.get("date")
        heure = request.POST.get("heure")
        medecin_id = request.POST.get("medecin")

        # 🔒 Bloquer les doublons (même médecin, même date, même heure)
        if RendezVous.objects.filter(
            medecin_id=medecin_id,
            date=date,
            heure=heure
        ).exists():
            return render(request, 'rdv/rendezvous.html', {
                'medecins': medecins,
                'erreur': "Ce créneau est déjà réservé. Choisissez une autre heure."
            })

        RendezVous.objects.create(
            patient=patient,
            date=date,
            heure=heure,
            medecin_id=medecin_id
        )

        return render(request, 'rdv/succes.html')

    return render(request, 'rdv/rendezvous.html', {'medecins': medecins})


# ================== ADMIN ==================
@login_required
def dashboard(request):
    return render(request, 'rdv/dashboard.html')


@login_required
def liste_rdv(request):
    rdvs = RendezVous.objects.all().order_by('-date', '-heure')
    return render(request, 'rdv/liste.html', {'rdvs': rdvs})


@login_required
def modifier_rdv(request, id):
    rdv = get_object_or_404(RendezVous, id=id)
    medecins = Medecin.objects.all()

    if request.method == "POST":
        rdv.patient = request.POST.get("patient")
        rdv.date = request.POST.get("date")
        rdv.heure = request.POST.get("heure")
        rdv.medecin_id = request.POST.get("medecin")
        rdv.save()
        return redirect('liste_rdv')

    return render(request, 'rdv/modifier.html', {'rdv': rdv, 'medecins': medecins})


@login_required
def supprimer_rdv(request, id):
    rdv = get_object_or_404(RendezVous, id=id)
    rdv.delete()
    return redirect('liste_rdv')


def deconnexion(request):
    logout(request)
    return redirect('login')
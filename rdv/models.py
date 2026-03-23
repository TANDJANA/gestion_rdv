from django.db import models

class Hopital(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.TextField()

    def __str__(self):
        return self.nom


class Medecin(models.Model):
    nom = models.CharField(max_length=100)
    specialite = models.CharField(max_length=100)
    hopital = models.ForeignKey(Hopital, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom


class RendezVous(models.Model):
    patient = models.CharField(max_length=100)
    medecin = models.ForeignKey(Medecin, on_delete=models.CASCADE,null=True, blank=True)
    date = models.DateField()
    heure = models.TimeField()
    statut = models.CharField(max_length=20, default="en attente")

    def __str__(self):
        return f"{self.patient} - {self.date}"
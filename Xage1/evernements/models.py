from django.db import models

class Evenement(models.Model):
    nom = models.CharField(max_length=200)
    description = models.TextField()
    pdf = models.FileField(upload_to='evernements/pdfs/')  # Assurez-vous d'avoir 'Pillow' installé pour gérer les images.
    photo = models.ImageField(upload_to='evernements/photos/')  
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()

    def __str__(self):
        return self.nom

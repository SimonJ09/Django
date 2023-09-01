from django.db import models

class Article(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    auteur = models.TextField()
    photo = models.ImageField(upload_to='articles/photos/')  # Assurez-vous d'avoir 'Pillow' installé pour gérer les images.
    pdf = models.FileField(upload_to='articles/pdfs/')
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titre

from django.db import models

class MonModel(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    age = models.IntegerField()
    sexe = models.CharField(max_length=1, choices=[('M', 'Masculin'), ('F', 'Féminin')])
    email = models.EmailField()
    profession = models.CharField(max_length=100)
    pays = models.CharField(max_length=100)
    situation_matrimoniale = models.CharField(
        max_length=1,
        choices=[('C', 'Célibataire'), ('M', 'Marié(e)'), ('D', 'Divorcé(e)'), ('V', 'Veuf/Veuve')]
    )
    contact = models.TextField()

    def __str__(self):
        return f"{self.nom} {self.prenom}"

from django.db import models


# Créer le modèle Recette
class Recette(models.Model):
    nom_agent = models.CharField(max_length=255)
    nom_plat = models.CharField(max_length=255)
    url_video = models.CharField(max_length=255)
    ingredients = models.JSONField()
    etapes_preparation = models.JSONField()
    time = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom_plat

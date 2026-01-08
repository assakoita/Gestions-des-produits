from django.db import models
from produits.models import Produit
from django.contrib.auth.models import User

class Commande(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    produits = models.ManyToManyField(Produit)
    date_commande = models.DateTimeField(auto_now_add=True)
    termine = models.BooleanField(default=False)

    def __str__(self):
        return f"Commande {self.id} - {self.client.username}"

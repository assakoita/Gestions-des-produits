from django.urls import path
from . import views

urlpatterns = [
    path('ajouter/<int:produit_id>/', views.ajouter_commande, name='ajouter_commande'),
    path('panier/', views.panier, name='panier'),
    path('valider/', views.valider_commande, name='valider_commande'),
]

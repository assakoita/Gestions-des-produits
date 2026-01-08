from django.shortcuts import render, redirect
from .models import Commande
from produits.models import Produit
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from types import SimpleNamespace

def ajouter_commande(request, produit_id):
    produit = Produit.objects.get(id=produit_id)
    # Si l'utilisateur est authentifié, enregistrer l'article dans la Commande en base
    if request.user.is_authenticated:
        commande, created = Commande.objects.get_or_create(client=request.user, termine=False)
        commande.produits.add(produit)
        messages.success(request, "Produit ajouté au panier.")
        return redirect('panier')

    # Pour les utilisateurs anonymes, conserver une liste d'IDs de produits dans la session
    panier = request.session.get('panier', [])
    # s'assurer que ce sont des entiers et éviter les doublons
    try:
        pid = int(produit_id)
    except (TypeError, ValueError):
        return redirect('liste_produits')
    if pid not in panier:
        panier.append(pid)
        request.session['panier'] = panier
        messages.success(request, "Produit ajouté au panier (session).")
    else:
        messages.info(request, "Le produit est déjà dans votre panier.")
    return redirect('panier')

def panier(request):
    # Utilisateurs authentifiés : afficher la Commande en base
    if request.user.is_authenticated:
        commande = Commande.objects.filter(client=request.user, termine=False).first()
        return render(request, 'commandes/panier.html', {'commande': commande})

    # Utilisateurs anonymes : construire un objet léger exposant `.produits`
    panier_ids = request.session.get('panier', [])
    if panier_ids:
        produits = Produit.objects.filter(id__in=panier_ids)
        guest_commande = SimpleNamespace(produits=produits)
        return render(request, 'commandes/panier.html', {'commande': guest_commande})

    # panier de session vide
    return render(request, 'commandes/panier.html', {'commande': None})

def valider_commande(request):
    # Si l'utilisateur n'est pas authentifié, le rediriger vers la page de connexion
    # avec un paramètre `next` pour qu'il soit renvoyé ici après connexion.
    if not request.user.is_authenticated:
        # Rediriger vers une petite page de choix proposant de se connecter ou de s'inscrire,
        # en conservant l'URL `next` pour que l'utilisateur revienne ici après authentification.
        next_url = reverse('valider_commande')
        auth_choice_url = reverse('auth_choice')
        return redirect(f"{auth_choice_url}?next={next_url}")

    commande = Commande.objects.filter(client=request.user, termine=False).first()
    if commande:
        commande.termine = True
        commande.save()
    return redirect('liste_produits')

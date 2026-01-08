from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.http import require_POST
from django.contrib import messages
from .models import Produit
from .forms import ProduitForm




def accueil(request):
    
    produits = Produit.objects.all()
    return render(request, 'produits/index.html', {'produits': produits})


def liste_produits(request):
    
    produits = Produit.objects.all()
    return render(request, 'produits/liste.html', {'produits': produits})


@staff_member_required(login_url='/utilisateurs/connexion/')
def ajouter_produit(request):
    
    if request.method == 'POST':
        form = ProduitForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Produit ajouté avec succès !")
            return redirect('liste_produits')
    else:
        form = ProduitForm()
    return render(request, 'produits/formulaire.html', {'form': form})


@staff_member_required(login_url='/utilisateurs/connexion/')
def modifier_produit(request, pk):
    
    
    produit = get_object_or_404(Produit, pk=pk)
    if request.method == 'POST':
        form = ProduitForm(request.POST, request.FILES, instance=produit)
        if form.is_valid():
            form.save()
            messages.success(request, "Produit modifié avec succès !")
            return redirect('liste_produits')
    else:
        form = ProduitForm(instance=produit)
    return render(request, 'produits/formulaire.html', {'form': form})


@require_POST
@staff_member_required(login_url='/utilisateurs/connexion/')
def supprimer_produit(request, pk):
    
    produit = get_object_or_404(Produit, pk=pk)
    produit.delete()
    messages.success(request, "Produit supprimé avec succès !")
    return redirect('liste_produits')

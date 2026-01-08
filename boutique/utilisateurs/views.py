from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.urls import reverse

def inscription(request):
    # conserver `next` afin qu'après l'inscription l'utilisateur puisse être redirigé vers la page de connexion
    next_url = request.POST.get('next') or request.GET.get('next')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Ne pas connecter automatiquement l'utilisateur ; le rediriger
            # vers la page de connexion pour qu'il s'authentifie explicitement.
            messages.success(request, "Compte créé avec succès. Connectez-vous.")
            # inclure `next` lors de la redirection vers la page de connexion
            if next_url:
                return redirect(f"{reverse('connexion')}?next={next_url}")
            return redirect('connexion')
    else:
        form = CustomUserCreationForm()
    
    for f in form.fields.values():
        existing = f.widget.attrs.get('class', '')
        if 'form-control' not in existing:
            f.widget.attrs['class'] = (existing + ' form-control').strip()
    return render(request, 'utilisateurs/inscription.html', {'form': form, 'next': next_url})

def connexion(request):
    
    next_url = request.POST.get('next') or request.GET.get('next')
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(next_url or 'liste_produits')
    else:
        form = AuthenticationForm()

    # ajouter la classe Bootstrap aux widgets du formulaire de connexion
    for f in form.fields.values():
        existing = f.widget.attrs.get('class', '')
        if 'form-control' not in existing:
            f.widget.attrs['class'] = (existing + ' form-control').strip()

    return render(request, 'utilisateurs/connexion.html', {'form': form, 'next': next_url})


def auth_choice(request):
    
    next_url = request.GET.get('next')
    return render(request, 'utilisateurs/auth_choice.html', {'next': next_url})

@require_POST
def deconnexion(request):
    """Déconnecte l'utilisateur actuel. N'accepte que les requêtes POST."""
    logout(request)
    return redirect('liste_produits')

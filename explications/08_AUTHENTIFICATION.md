# 8. L'AUTHENTIFICATION (Connexion / Inscription)

## 8.1 C'est quoi l'authentification ?

C'est le système qui permet aux utilisateurs de :

1. **S'inscrire** (créer un compte)
2. **Se connecter** (entrer dans leur compte)
3. **Se déconnecter** (sortir)

Django fournit tout ça déjà prêt !

---

## 8.2 Le modèle User (Utilisateur)

Django a un modèle `User` avec ces infos :

| Champ | C'est quoi ? |
|-------|-------------|
| `username` | Nom d'utilisateur |
| `password` | Mot de passe (crypté) |
| `email` | Adresse email |
| `is_staff` | Est-ce un admin ? (True/False) |
| `is_active` | Compte actif ? (True/False) |

---

## 8.3 L'inscription

📍 Fichier : `utilisateurs/views.py`

```python
def inscription(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Crée le compte
            return redirect('connexion')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'utilisateurs/inscription.html', {'form': form})
```

### 8.3.1 Ce qui se passe :

| Étape | Action |
|-------|--------|
| 1 | L'utilisateur remplit le formulaire |
| 2 | Django vérifie (mot de passe assez fort, etc.) |
| 3 | Le compte est créé dans la base de données |
| 4 | On redirige vers la page de connexion |

---

## 8.4 La connexion

```python
from django.contrib.auth import login

def connexion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)  # Connecte l'utilisateur !
            return redirect('liste_produits')
    else:
        form = AuthenticationForm()
    
    return render(request, 'utilisateurs/connexion.html', {'form': form})
```

### 8.4.1 Ce qui se passe :

| Étape | Action |
|-------|--------|
| 1 | L'utilisateur entre son nom et mot de passe |
| 2 | Django vérifie dans la base de données |
| 3 | `login()` crée une session (l'utilisateur est connecté) |
| 4 | À partir de maintenant, `request.user` = cet utilisateur |

---

## 8.5 La déconnexion

```python
from django.contrib.auth import logout

def deconnexion(request):
    logout(request)  # Déconnecte
    return redirect('liste_produits')
```

---

## 8.6 Vérifier si connecté

### 8.6.1 Dans une vue :

```python
def ma_vue(request):
    if request.user.is_authenticated:
        # L'utilisateur est connecté
        print(request.user.username)
    else:
        # C'est un visiteur anonyme
        pass
```

### 8.6.2 Dans un template :

```html
{% if user.is_authenticated %}
    <p>Bonjour {{ user.username }} !</p>
    <a href="{% url 'deconnexion' %}">Déconnexion</a>
{% else %}
    <a href="{% url 'connexion' %}">Connexion</a>
{% endif %}
```

---

## 8.7 Protéger une page

### 8.7.1 Page réservée aux utilisateurs connectés :

```python
from django.contrib.auth.decorators import login_required

@login_required
def ma_page_protegee(request):
    # Seuls les connectés peuvent accéder
    pass
```

### 8.7.2 Page réservée aux admins :

```python
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def ma_page_admin(request):
    # Seuls les admins peuvent accéder
    pass
```

---

## 8.8 Résumé des décorateurs

| Décorateur | Qui peut accéder ? |
|------------|-------------------|
| Aucun | Tout le monde |
| `@login_required` | Connectés seulement |
| `@staff_member_required` | Admins seulement |

---

## 8.9 Créer un admin

Dans le terminal :

```bash
python manage.py createsuperuser
```

Tu entres :
- Nom d'utilisateur
- Email
- Mot de passe

Cet utilisateur aura `is_staff = True` et pourra gérer les produits.

# 4. LES VIEWS (La Logique)

## 4.1 C'est quoi une vue ?

Une vue c'est une **fonction Python** qui :

1. Reçoit une demande (l'utilisateur visite une page)
2. Fait quelque chose (chercher des données, enregistrer...)
3. Renvoie une réponse (une page HTML)

📍 Fichier : `produits/views.py`

---

## 4.2 Exemple simple

```python
def liste_produits(request):
    # 1. Récupérer tous les produits
    produits = Produit.objects.all()
    
    # 2. Afficher la page avec les produits
    return render(request, 'produits/liste.html', {'produits': produits})
```

### 4.2.1 Explication ligne par ligne :

| Ligne | Ça fait quoi ? |
|-------|---------------|
| `def liste_produits(request):` | On crée une fonction appelée "liste_produits" |
| `Produit.objects.all()` | On récupère TOUS les produits de la base |
| `render(...)` | On affiche la page HTML avec les produits |

---

## 4.3 Les permissions (qui peut faire quoi ?)

### 4.3.1 Vue accessible à TOUT LE MONDE :

```python
def liste_produits(request):
    # Pas de protection, tout le monde peut voir
    produits = Produit.objects.all()
    return render(request, 'produits/liste.html', {'produits': produits})
```

### 4.3.2 Vue réservée aux ADMINS :

```python
@staff_member_required
def ajouter_produit(request):
    # Seuls les admins peuvent accéder
    # Les autres sont redirigés vers la connexion
    ...
```

Le `@staff_member_required` veut dire : "Seuls les admins peuvent accéder à cette page"

---

## 4.4 Tableau des permissions du projet

| Vue | Qui peut y accéder ? |
|-----|---------------------|
| `accueil` | Tout le monde |
| `liste_produits` | Tout le monde |
| `ajouter_produit` | **Admins seulement** |
| `modifier_produit` | **Admins seulement** |
| `supprimer_produit` | **Admins seulement** |
| `panier` | Tout le monde |
| `valider_commande` | Clients connectés |

---

## 4.5 Comment créer un admin ?

Dans le terminal :

```bash
python manage.py createsuperuser
```

Tu entres un nom, email et mot de passe. Cet utilisateur pourra gérer les produits.

---

## 4.6 Les fonctions utiles

| Fonction | Ça fait quoi ? |
|----------|---------------|
| `render()` | Affiche une page HTML |
| `redirect()` | Redirige vers une autre page |
| `get_object_or_404()` | Cherche un objet ou affiche erreur 404 |
| `messages.success()` | Affiche un message de succès |

---

## 4.7 L'objet request (la demande)

Quand quelqu'un visite une page, Django reçoit une `request` avec des infos :

| Info | Ça donne quoi ? |
|------|----------------|
| `request.method` | "GET" (visite) ou "POST" (formulaire envoyé) |
| `request.user` | L'utilisateur connecté |
| `request.user.is_authenticated` | `True` si connecté |
| `request.user.is_staff` | `True` si c'est un admin |

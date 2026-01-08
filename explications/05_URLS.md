# 5. LES URLS (Les Adresses Web)

## 5.1 C'est quoi une URL ?

Une URL c'est l'**adresse** d'une page web.

Exemple : `http://127.0.0.1:8001/produits/`

Le fichier `urls.py` dit à Django : "Quand quelqu'un va à cette adresse, affiche cette page."

---

## 5.2 Le fichier urls.py principal

📍 Fichier : `boutique/boutique/urls.py`

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('produits.urls')),
    path('utilisateurs/', include('utilisateurs.urls')),
    path('commandes/', include('commandes.urls')),
]
```

### 5.2.1 Explication ligne par ligne :

| Ligne | Ça fait quoi ? |
|-------|---------------|
| `path('admin/', ...)` | `/admin/` → Interface d'administration |
| `path('', include('produits.urls'))` | `/` → Va chercher dans `produits/urls.py` |
| `path('utilisateurs/', ...)` | `/utilisateurs/...` → Va chercher dans `utilisateurs/urls.py` |
| `path('commandes/', ...)` | `/commandes/...` → Va chercher dans `commandes/urls.py` |

---

## 5.3 Comment ça marche ?

Quand tu tapes `http://127.0.0.1:8001/utilisateurs/connexion/` :

1. Django regarde le fichier `urls.py` principal
2. Il voit que `/utilisateurs/` renvoie vers `utilisateurs/urls.py`
3. Dans `utilisateurs/urls.py`, il trouve `connexion/`
4. Il appelle la fonction `connexion()` dans `views.py`
5. La page s'affiche !

---

## 5.4 Toutes les URLs du projet

| Adresse | Page affichée |
|---------|--------------|
| `/` | Accueil |
| `/produits/` | Liste des produits |
| `/ajouter/` | Formulaire ajouter produit (admin) |
| `/modifier/5/` | Modifier le produit n°5 (admin) |
| `/supprimer/5/` | Supprimer le produit n°5 (admin) |
| `/utilisateurs/inscription/` | Page d'inscription |
| `/utilisateurs/connexion/` | Page de connexion |
| `/commandes/panier/` | Voir le panier |
| `/admin/` | Interface d'administration |

---

## 5.5 Les paramètres dans les URLs

Parfois l'URL contient une valeur variable :

```python
path('modifier/<int:pk>/', views.modifier_produit, name='modifier_produit')
```

| Partie | Signification |
|--------|--------------|
| `modifier/` | Le début de l'URL |
| `<int:pk>` | Un nombre (l'id du produit) |
| `views.modifier_produit` | La fonction à appeler |
| `name='modifier_produit'` | Le nom pour référencer cette URL |

Exemple : `/modifier/5/` → `pk = 5` → Modifier le produit n°5

---

## 5.6 Utiliser les URLs dans les templates

```html
<!-- Lien simple -->
<a href="{% url 'liste_produits' %}">Voir les produits</a>

<!-- Lien avec paramètre -->
<a href="{% url 'modifier_produit' pk=produit.id %}">Modifier</a>
```

Le `{% url 'nom' %}` génère automatiquement la bonne adresse.

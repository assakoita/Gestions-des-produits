# 7. LES FORMULAIRES

## 7.1 C'est quoi un formulaire Django ?

Un formulaire Django c'est une **classe** qui :

1. Génère le HTML des champs (input, textarea...)
2. Vérifie que les données sont correctes
3. Peut sauvegarder directement en base de données

📍 Fichier : `produits/forms.py`

---

## 7.2 Créer un formulaire

### 7.2.1 Formulaire basé sur un modèle (le plus simple)

```python
from django import forms
from .models import Produit

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ['nom', 'description', 'prix', 'disponible', 'image']
```

| Partie | Signification |
|--------|--------------|
| `model = Produit` | Ce formulaire est pour le modèle Produit |
| `fields = [...]` | Les champs à afficher dans le formulaire |

Django crée automatiquement les inputs HTML !

---

## 7.3 Utiliser le formulaire dans la vue

```python
def ajouter_produit(request):
    if request.method == 'POST':
        # L'utilisateur a cliqué sur "Envoyer"
        form = ProduitForm(request.POST, request.FILES)
        
        if form.is_valid():
            # Les données sont correctes → Sauvegarder
            form.save()
            return redirect('liste_produits')
    else:
        # L'utilisateur vient d'arriver → Formulaire vide
        form = ProduitForm()
    
    return render(request, 'produits/formulaire.html', {'form': form})
```

### 7.3.1 Explication étape par étape :

| Étape | Ce qui se passe |
|-------|----------------|
| 1 | L'utilisateur visite la page (GET) |
| 2 | On affiche un formulaire vide |
| 3 | L'utilisateur remplit et clique "Envoyer" (POST) |
| 4 | On vérifie les données avec `form.is_valid()` |
| 5 | Si OK → On sauvegarde et on redirige |
| 6 | Si erreur → On réaffiche le formulaire avec les erreurs |

---

## 7.4 Afficher le formulaire dans le template

### 7.4.1 Méthode simple

```html
<form method="post" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Enregistrer</button>
</form>
```

### 7.4.2 Méthode personnalisée (plus joli)

```html
<form method="post" enctype="multipart/form-data">
    {% csrf_token %}
    
    {% for field in form %}
        <div class="mb-3">
            <label>{{ field.label }}</label>
            {{ field }}
            
            {% for error in field.errors %}
                <span class="erreur">{{ error }}</span>
            {% endfor %}
        </div>
    {% endfor %}
    
    <button type="submit">Enregistrer</button>
</form>
```

---

## 7.5 Les points importants

### 7.5.1 Ne jamais oublier `{% csrf_token %}`

```html
<form method="post">
    {% csrf_token %}   <!-- OBLIGATOIRE ! -->
    ...
</form>
```

Sans ça → Erreur 403 interdite !

---

### 7.5.2 Pour les images : `enctype="multipart/form-data"`

```html
<form method="post" enctype="multipart/form-data">
```

Et dans la vue :

```python
form = ProduitForm(request.POST, request.FILES)  # request.FILES pour les images
```

---

## 7.6 Résumé

| Ce que tu veux faire | Comment faire |
|---------------------|---------------|
| Créer un formulaire | Créer une classe dans `forms.py` |
| L'afficher | `{{ form.as_p }}` dans le template |
| Le traiter | `form.is_valid()` puis `form.save()` |
| Protéger | `{% csrf_token %}` dans le template |
| Envoyer des images | `enctype="multipart/form-data"` |

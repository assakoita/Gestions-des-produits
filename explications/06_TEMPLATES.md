# 6. LES TEMPLATES (Les Pages HTML)

## 6.1 C'est quoi un template ?

Un template c'est un fichier **HTML** avec des parties dynamiques.

Exemple : Une page qui affiche les produits. Le HTML est le même, mais les produits changent.

📍 Dossier : `produits/templates/produits/`

---

## 6.2 Les balises spéciales Django

### 6.2.1 Afficher une variable : `{{ }}`

```html
<h1>{{ produit.nom }}</h1>
<p>Prix : {{ produit.prix }} €</p>
```

Les `{{ }}` affichent le contenu d'une variable.

---

### 6.2.2 Faire de la logique : `{% %}`

```html
{% if user.is_authenticated %}
    <p>Bonjour {{ user.username }}</p>
{% else %}
    <p>Connectez-vous</p>
{% endif %}
```

Les `{% %}` permettent de faire des conditions et des boucles.

---

## 6.3 La boucle FOR

Pour afficher une liste de produits :

```html
{% for produit in produits %}
    <div class="card">
        <h2>{{ produit.nom }}</h2>
        <p>{{ produit.prix }} €</p>
    </div>
{% endfor %}
```

| Partie | Signification |
|--------|--------------|
| `{% for produit in produits %}` | Pour chaque produit dans la liste... |
| `{{ produit.nom }}` | Affiche le nom du produit |
| `{% endfor %}` | Fin de la boucle |

---

## 6.4 La condition IF

```html
{% if produit.disponible %}
    <span class="vert">En stock</span>
{% else %}
    <span class="rouge">Rupture</span>
{% endif %}
```

| Partie | Signification |
|--------|--------------|
| `{% if ... %}` | Si la condition est vraie... |
| `{% else %}` | Sinon... |
| `{% endif %}` | Fin de la condition |

---

## 6.5 L'héritage de templates

### 6.5.1 Le template de base (base.html)

C'est le modèle commun à toutes les pages :

```html
<!DOCTYPE html>
<html>
<head>
    <title>Boutique</title>
</head>
<body>
    <nav>Menu ici...</nav>
    
    {% block content %}
    <!-- Les pages enfants mettent leur contenu ici -->
    {% endblock %}
    
    <footer>Pied de page</footer>
</body>
</html>
```

### 6.5.2 Une page qui utilise le modèle

```html
{% extends 'base.html' %}

{% block content %}
    <h1>Liste des produits</h1>
    <!-- Mon contenu spécifique -->
{% endblock %}
```

| Partie | Signification |
|--------|--------------|
| `{% extends 'base.html' %}` | J'utilise le modèle base.html |
| `{% block content %}` | Je mets mon contenu dans cette zone |

---

## 6.6 Les liens et URLs

```html
<!-- Lien vers une page -->
<a href="{% url 'liste_produits' %}">Produits</a>

<!-- Lien avec paramètre -->
<a href="{% url 'modifier_produit' pk=5 %}">Modifier</a>
```

---

## 6.7 Le CSRF Token (OBLIGATOIRE dans les formulaires)

```html
<form method="post">
    {% csrf_token %}
    <!-- Les champs du formulaire -->
    <button type="submit">Envoyer</button>
</form>
```

Le `{% csrf_token %}` protège contre les attaques. **Ne jamais l'oublier !**

---

## 6.8 Les messages flash

Pour afficher des messages de succès/erreur :

```html
{% if messages %}
    {% for message in messages %}
        <div class="alert">{{ message }}</div>
    {% endfor %}
{% endif %}
```

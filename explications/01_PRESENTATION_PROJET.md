# 1. PRÉSENTATION DU PROJET

 1.1 C'est quoi ce projet ?

C'est une **boutique en ligne** simple. Elle permet de :

1. Voir des produits
2. Ajouter des produits au panier
3. Créer un compte client
4. Passer des commandes

---

## 1.2 Comment sont organisés mes dossiers ?

```
GestionDesProduits/
│
├── boutique/           → Le projet Django
│   ├── boutique/       → Configuration (réglages)
│   ├── produits/       → Tout ce qui concerne les produits
│   ├── commandes/      → Tout ce qui concerne le panier
│   ├── utilisateurs/   → Inscription et connexion
│   └── media/          → Les images des produits
│
├── explications/       → Ce dossier (documentation)
└── my_env/             → Python (ne pas toucher)
```

---

## 1.3 Qui peut faire quoi ?

| Personne | Ce qu'elle peut faire |
|----------|----------------------|
| **Visiteur** (pas connecté) | Voir les produits, ajouter au panier |
| **Client** (connecté) | Voir les produits, ajouter au panier, passer commande |
| **Admin** (staff) | Ajouter, modifier, supprimer des produits |

---

## 1.4 Comment démarrer le projet ?

Ouvre le terminal et tape ces commandes :

```bash
# 1. Activer l'environnement Python
source /Users/user/Desktop/GestionDesProduits/my_env/bin/activate

# 2. Aller dans le dossier du projet
cd /Users/user/Desktop/GestionDesProduits/boutique

# 3. Lancer le serveur
python manage.py runserver 8001
```

Ensuite ouvre ton navigateur et va sur : **http://127.0.0.1:8001/**

# 2. LE FICHIER SETTINGS.PY (Les Réglages)

## 2.1 C'est quoi ce fichier ?

C'est le fichier de **configuration** du projet. Il contient tous les réglages.

📍 Où il se trouve : `boutique/boutique/settings.py`

---

## 2.2 Les réglages importants

### 2.2.1 DEBUG (Mode développement)

```python
DEBUG = True
```

- `True` = Tu es en train de développer. Les erreurs s'affichent en détail.
- `False` = Site en production (en ligne). Ne jamais montrer les erreurs.

---

### 2.2.2 INSTALLED_APPS (Les applications)

```python
INSTALLED_APPS = [
    'produits',        # Notre app pour les produits
    'commandes',       # Notre app pour le panier
    'utilisateurs',    # Notre app pour les comptes
]
```

C'est la liste des applications activées dans le projet.

---

### 2.2.3 DATABASES (La base de données)

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Type : MySQL
        'NAME': 'boutique_db',                  # Nom de la base
        'USER': 'root',                         # Utilisateur
        'PASSWORD': 'root',                     # Mot de passe
        'HOST': 'localhost',                    # Adresse
        'PORT': '8889',                         # Port MAMP
    }
}
```

C'est ici qu'on dit à Django comment se connecter à la base de données.

---

### 2.2.4 MEDIA (Les images)

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

- `MEDIA_URL` : L'adresse web pour voir les images → `/media/`
- `MEDIA_ROOT` : Le dossier où Django stocke les images → `boutique/media/`

---

## 2.3 Résumé simple

| Réglage | Ça fait quoi ? |
|---------|---------------|
| `DEBUG` | Mode développement oui/non |
| `INSTALLED_APPS` | Liste des applications |
| `DATABASES` | Connexion à la base de données |
| `MEDIA_URL` | Adresse des images |

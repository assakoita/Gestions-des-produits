# 3. LES MODELS (La Base de Données)

## 3.1 C'est quoi un modèle ?

Un modèle c'est une **table** dans la base de données.

Exemple simple :
- Tu veux stocker des produits → Tu crées un modèle `Produit`
- Chaque produit a un nom, un prix, une image → Ce sont les **colonnes** de la table

---

## 3.2 Le modèle Produit

📍 Fichier : `produits/models.py`

```python
class Produit(models.Model):
    nom = models.CharField(max_length=100)      # Texte court
    description = models.TextField()             # Texte long
    prix = models.DecimalField(...)             # Nombre avec virgule
    disponible = models.BooleanField()          # Oui ou Non
    image = models.ImageField()                 # Image
```

### 3.2.1 Ce que ça crée dans la base de données :

| Colonne | Type | Exemple |
|---------|------|---------|
| id | Nombre | 1, 2, 3... (automatique) |
| nom | Texte | "T-shirt bleu" |
| description | Texte long | "Un beau t-shirt..." |
| prix | Nombre | 19.99 |
| disponible | Oui/Non | True |
| image | Chemin | "produits/tshirt.jpg" |

---

## 3.3 Le modèle Commande

📍 Fichier : `commandes/models.py`

```python
class Commande(models.Model):
    client = models.ForeignKey(User, ...)       # Qui a commandé
    produits = models.ManyToManyField(Produit)  # Les produits commandés
    date_commande = models.DateTimeField()      # Quand
    termine = models.BooleanField()             # Commande terminée ?
```

### 3.3.1 Explication simple :

- `client` : Une commande appartient à **UN** client
- `produits` : Une commande peut avoir **PLUSIEURS** produits
- `termine` : `False` = panier en cours, `True` = commande validée

---

## 3.4 Les types de champs courants

| Type | C'est quoi ? | Exemple |
|------|-------------|---------|
| `CharField` | Texte court | nom, titre |
| `TextField` | Texte long | description |
| `IntegerField` | Nombre entier | quantité, âge |
| `DecimalField` | Nombre à virgule | prix |
| `BooleanField` | Oui ou Non | actif, disponible |
| `DateTimeField` | Date et heure | date_creation |
| `ImageField` | Image | photo |
| `ForeignKey` | Lien vers 1 autre | client → User |
| `ManyToManyField` | Lien vers plusieurs | produits |

---

## 3.5 Commandes à retenir

Après avoir modifié un modèle, tape ces commandes :

```bash
# 1. Préparer les changements
python manage.py makemigrations

# 2. Appliquer à la base de données
python manage.py migrate
```

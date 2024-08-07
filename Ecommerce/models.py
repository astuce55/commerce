from django.db import models # type: ignore

# Create your models here.

class Produit(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    qte_stock = models.PositiveIntegerField(default=0)


class ProduitImages(models.Model):
    produit = models.ForeignKey(Produit, on_delete= models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='produit_images')


class Client(models.Model):
    nom = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    adresse = models.CharField(max_length=200)


class commande(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)


class Facture(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    Total = models.DecimalField(max_digits=10, decimal_places=2) # Montant total à payer


class Details(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    Facture = models.ForeignKey(Facture, on_delete=models.CASCADE)
    qté = models.PositiveIntegerField(default=0)
    prix_total = models.DecimalField(max_digits=10, decimal_places=2) # Prix total pour un produit commandé



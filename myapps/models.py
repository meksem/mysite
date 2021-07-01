# Create your models here.
from django.db import models


'''from phonenumber_field.modelfields import PhoneNumberField'''


class Devis(models.Model):
    date_devis = models.DateTimeField(auto_now_add=True)
    firstname = models.CharField(max_length=100, unique=True)
    lastname = models.CharField(max_length=200, unique=True)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=12)
    website = models.URLField(max_length=200,)
    statut = models.CharField(max_length=255, verbose_name="state")
    description = models.TextField()

    def __str__(self):
        return str(self.date_devis)


class DevisDemande(models.Model):
    date_devis = models.DateTimeField(auto_now_add=True)
    firstname = models.CharField(max_length=100, unique=True)
    lastname = models.CharField(max_length=200, unique=True)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=12)
    pack_choice=models.EmailField(max_length=254)
    statut = models.CharField(max_length=255, verbose_name="state")
    description = models.TextField()
            
    def __str__(self):
        return str(self.date_devis)

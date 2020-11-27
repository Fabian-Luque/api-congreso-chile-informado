from django.db import models

# Create your models here.

class Congressman(models.Model):
    name = models.CharField(max_length=250)
    district  = models.IntegerField()
    num_congress = models.IntegerField()
    entity = models.CharField(max_length=50)
    suplent = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    foto = models.URLField(max_length=500)
    politicalParty = models.ForeignKey(
        "PoliticalParty",
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    commission = models.ForeignKey(
        "Commission", 
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name


class PoliticalParty(models.Model):
    name = models.CharField(max_length=250)
    descripton = models.TextField()
    status = models.CharField(max_length=50)
    orientation = models.SmallIntegerField()
    establish = models.DateField()
    president = models.OneToOneField(
        "Congressman", 
        on_delete=models.CASCADE,
        related_name='%(class)s_president'
    )

    def __str__(self):
        return self.name


class Commission(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    president = models.OneToOneField(
        "Congressman", 
        on_delete=models.CASCADE,
        related_name='%(class)s_president'
    )

    def __str__(self):
        return self.name



    

from django.db import models

# Create your models here.
class OrderItem(models.Model):
    Oname = models.CharField(max_length=20, null=False)
    Otemperature = models.CharField(max_length=20, null=False)
    Ocupnumber = models.IntegerField(null=False)
    Oodertime = models.DateTimeField(max_length=50, auto_now_add=True)

    def __str__(self):
        return self.Oname
    

class CoffeeBeanItem(models.Model):
    CBname = models.CharField(max_length=50, null=False)
    CBcoffeeshop = models.CharField(max_length=50, null=False)
    CBplace = models.CharField(max_length=50, null=False)
    CBroasting = models.CharField(max_length=50, null=False)
    CBprice = models.CharField(max_length=50, null=False)
    CBflavor = models.CharField(max_length=50, null=False)
    CBurl = models.CharField(max_length=200, null=False)
    CBcoffeetoday = models.CharField(max_length=10, null=False)

    def __str__(self):
        return self.CBname
from django.db import models


class Product(models.Model):
    Date=models.DateField()
    Provider=models.CharField(max_length=20)
    Nameofproduct=models.CharField(max_length=30)
    Price=models.FloatField()
    Quantity=models.FloatField()
    Amount=models.FloatField()
    Stock=models.FloatField()





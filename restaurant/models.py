from django.db import models

# Create your models here.

class RestaurantDeshboardData(models.Model):

    name = models.CharField(max_length=100, null=True,  blank=True, default=None)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField(null=True,  blank=True, default=None)
    price = models.IntegerField(null=True,  blank=True, default=None)
    offer = models.BooleanField(default=False)
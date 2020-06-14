from django.db import models

# Create your models here.

class RestaurantDeshboardData(models.Model):

    name = models.CharField(max_length=100, null=True,  blank=True, default=None)
    img = models.ImageField(upload_to='pics',blank=True, null=True, default=None)
    desc = models.TextField(null=True,  blank=True, default=None)
    price = models.IntegerField(null=True,  blank=True, default=None)
    offer = models.BooleanField(default=False)

    @property
    def representation(self):
        return 'Name: {}'.format(self.name)

    class Meta:
        verbose_name = "Deshsboard data"
        verbose_name_plural = "Deshsboard data"

    def __str__(self):
        return self.representation
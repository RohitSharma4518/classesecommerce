from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class CustomManager(models.Manager):
    def mobile_list(self):
        return self.filter(category__exact="Mobile")

    def cloths_list(self):
        return self.filter(category__exact="Cloths")

    def shoes_list(self):
        return self.filter(category__exact="Shoes")

    def get_price_range(self, r1, r2):
        return self.filter(price__range=(r1, r2))


class Product(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    product_id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=55)
    type = (("Mobile", "Mobile"), ("Cloths", "Cloths"), ("Shoes", "Shoes"))
    category = models.CharField(max_length=50, choices=type, default="")
    desc = models.TextField(max_length=100)
    price = models.FloatField()
    image = models.ImageField(upload_to="pics")
    objects = models.Manager()
    prod = CustomManager()


class Cart(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    product_id = models.ForeignKey(
        Product, on_delete=models.CASCADE, null=True, blank=True
    )
    qty = models.PositiveIntegerField(default=0)


class Order(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    product_id = models.ForeignKey(
        Product, on_delete=models.CASCADE, null=True, blank=True
    )
    orderid = models.IntegerField(primary_key=True)
    qty = models.PositiveIntegerField(default=0)

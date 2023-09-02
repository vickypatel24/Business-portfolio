from django.db import models

# Create your models here.
class Member(models.Model):
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    age = models.IntegerField()

    # def __str__(self):
    #     return f"{self.f_name} {self.l_name} {self.age}"

class Products(models.Model):
    product_name = models.CharField(max_length=255)
    product_price = models.IntegerField(null=True)
    product_category = models.ForeignKey('Product_details', on_delete=models.CASCADE)
    product_description = models.TextField(max_length=255, null=True)
    timestamp = models.DateTimeField(auto_now=True)
    product_image = models.ImageField(upload_to='shop/images', null=True)

    def __str__(self):
        return self.product_name


class Product_details(models.Model):
    product_category = models.CharField(max_length=255)
    product_discount = models.IntegerField(null=True)

    def __str__(self):
        return self.product_category


class UserOtp(models.Model):
    objects = None
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    otp = models.IntegerField()

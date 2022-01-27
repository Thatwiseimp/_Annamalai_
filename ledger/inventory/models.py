from django.db import models
from django.core.validators import RegexValidator

class Variant(models.Model):
    Color = models.CharField(max_length=20,null=False)
    Price_per_unit=models.IntegerField(null=False)

    def __str__(self):
        return self.Color

class Customer(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    Customer_name = models.CharField(primary_key=True,max_length=50, unique=True, null=False, default='')
    Phone_number = models.CharField(validators=[phone_regex], max_length=10, blank=True)
    Date_of_subscription = models.DateField()
    Units = models.IntegerField()
    data = models.ForeignKey(Variant, on_delete=models.CASCADE)

    def __str__(self):
        return self.Customer_name

    def history(self):
        return self.data.Color

class Table(models.Model):
    Date= models.DateField()
    buyer = models.ForeignKey(Customer, on_delete=models.CASCADE)

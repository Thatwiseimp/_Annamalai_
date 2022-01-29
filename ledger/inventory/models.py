from django.db import models


class Customer(models.Model):
    Customer_name = models.CharField(max_length=50, null=False, default='')
    Phone_number = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.Customer_name


class PType(models.Model):
    label = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.label

class MConfig(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.PROTECT, null=True)
    packet = models.ForeignKey(PType, on_delete=models.PROTECT, null=True)
    quantity = models.IntegerField(null=True,default=0)

    def __str__(self):
        return self.user.Customer_name+' --> '+self.packet.label+'('+str(self.quantity)+')'
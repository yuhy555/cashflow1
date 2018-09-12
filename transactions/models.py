from django.db import models
from paymentmethod.models import  PaymentMethod
from location.models import  Location
from transactiontype.models import  TransactionType
from django.contrib.auth.models import User
# Create your models here.


class Transaction(models.Model):
    tran_date = models.DateTimeField()
    tran_amount = models.FloatField(default=0.00)
    tran_payment_method = models.ForeignKey(PaymentMethod,on_delete=models.SET_NULL,null=True)
    tran_location = models.ForeignKey(Location,on_delete=models.SET_NULL,null=True)
    tran_type = models.ForeignKey(TransactionType,on_delete=models.SET_NULL,null=True)
    account = models.ForeignKey(User,on_delete=models.CASCADE,default='')
    create_date = models.DateTimeField(auto_now_add=True, blank=True)


    def pub_date_pretty(self):
        return self.tran_date.strftime('%b %e %Y %I:%M %p')

    def datetime_local_value_format(self):
        return self.tran_date.strftime('%Y-%m-%dT%H:%M')
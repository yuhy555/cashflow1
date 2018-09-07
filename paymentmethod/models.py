from django.db import models

from django.contrib.auth.models import User
class PaymentMethod(models.Model):
    method_name=models.CharField(max_length=50)
    status = models.IntegerField(default=1) #0:inactive 1:active
    credit_limit=models.CharField(max_length=50)
    account = models.ForeignKey(User, on_delete=models.CASCADE,default='')
    create_date = models.DateTimeField()


from django.db import models
from datetime import datetime

class PaymentMethod(models.Model):
    method_name=models.CharField(max_length=50)
    status = models.IntegerField(default=1) #0:inactive 1:active
    credit_limit=models.CharField(max_length=50)
    create_date = models.DateTimeField(default=datetime.now, blank=True)


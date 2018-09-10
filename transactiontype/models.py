from django.db import models
from django.contrib.auth.models import User
class TransactionType(models.Model):
    name = models.CharField(max_length=200)
    status = models.IntegerField(default=1)  # 0:inactive 1:active
    income_ind=models.IntegerField(default=0) # 1: expense 2: income
    account = models.ForeignKey(User, on_delete=models.CASCADE,default='')
    create_date = models.DateTimeField(auto_now_add=True, blank=True)
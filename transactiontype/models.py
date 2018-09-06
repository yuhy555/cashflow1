from django.db import models

class TransactionType(models.Model):
    name = models.CharField(max_length=200)
    status = models.IntegerField(default=1)  # 0:inactive 1:active
    income_ind=models.IntegerField(default=0)
    create_date = models.DateTimeField(auto_now_add=True, blank=True)
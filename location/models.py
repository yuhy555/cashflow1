from django.db import models

class Location(models.Model):
    name=models.CharField(max_length=200)
    street = models.CharField(max_length=200,blank=True, default='')
    city = models.CharField(max_length=200,blank=True, default='')
    province = models.CharField(max_length=200,blank=True, default='')
    country = models.CharField(max_length=200,blank=True, default='')
    postal_code = models.CharField(max_length=10,blank=True, default='')
    status = models.IntegerField(default=1)  # 0:inactive 1:active
    create_date = models.DateTimeField(auto_now_add=True, blank=True)

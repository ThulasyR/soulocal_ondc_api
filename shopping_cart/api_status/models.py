from django.db import models

class ApiContextStatus(models.Model):
    STATUS_ID= models.CharField(max_length=250)
    STATUS_CODE= models.CharField(max_length=250,blank=True, null=True, default=None,)
    ORDER_ID= models.CharField(max_length=250,blank=True, null=True, default=None,)
    
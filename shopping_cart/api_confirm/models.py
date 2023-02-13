from django.db import models
from django.db import models

class ApiContextConfirm(models.Model):
    ORDER_ID= models.CharField(max_length=250)
    ORDER_NAME= models.CharField(max_length=250,blank=True, null=True, default=None,)
    ORDER_STATUS= models.CharField(max_length=250,blank=True, null=True, default=None,)
    PROVIDER_ID= models.CharField(max_length=250,blank=True, null=True, default=None,)
    ITEMS_ID= models.CharField(max_length=250,blank=True, null=True, default=None)
    BILLING_NAME= models.CharField(max_length=250,blank=True, null=True, default=None)
    BILLING_ORG_NAME= models.CharField(max_length=250,blank=True, null=True, default=None)
    BILLING_ORG_CRED= models.CharField(max_length=250,blank=True, null=True, default=None)
    BILLING_EMAILADDRESS= models.CharField(max_length=250,blank=True, null=True, default=None)
    BILLING_PHONE= models.CharField(max_length=250,blank=True, null=True, default=None)
    PAYMENT_TRANS_ID= models.CharField(max_length=250,blank=True, null=True, default=None)
    PAYMENT_TRANS_STATUS= models.CharField(max_length=250,blank=True, null=True, default=None)
    PAYMENT_TRANS_AMT= models.CharField(max_length=250,blank=True, null=True, default=None)
    PAYMENT_TRANS_CURRENCY= models.CharField(max_length=250,blank=True, null=True, default=None)
    PAYMENT_DATE= models.CharField(max_length=250,blank=True, null=True, default=None)
   
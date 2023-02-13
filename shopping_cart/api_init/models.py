from django.db import models
from django.db import models

class ApiContextInit(models.Model):
    BILLING_ID= models.CharField(max_length=250)
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
   
from django.db import models

class ApiContextModel(models.Model):
    domain = models.CharField(max_length=25)
    country= models.CharField(max_length=150)
    city= models.CharField(max_length=150)
    action= models.CharField(max_length=25)
    core_version= models.CharField(max_length=200)
    bap_id= models.CharField(max_length=200)
    bap_uri= models.CharField(max_length=200)
    bpp_id= models.CharField(max_length=200)
    bpp_uri= models.CharField(max_length=200)
    transaction_id= models.CharField(max_length=200)
    message_id= models.CharField(max_length=200)
    timestamp= models.CharField(max_length=200)
    key= models.CharField(max_length=500)
    ttl= models.CharField(max_length=500)
    
    
class ApiContextCategory(models.Model):
    CATEGORY_NAME= models.CharField(max_length=250)
    CATEGORY_CODE= models.CharField(max_length=250,blank=True, null=True, default=None,)
    CATEGORY_SYMBOL= models.CharField(max_length=250,blank=True, null=True, default=None,)
    CATEGORY_SHORTDESC= models.CharField(max_length=250,blank=True, null=True, default=None,)
    CATEGORY_LONGDESC= models.CharField(max_length=250,blank=True, null=True, default=None)
    CATEGORY_IMAGES= models.ImageField(upload_to='upload',blank=True, null=True, default=None)
    CATEGORY_TIMELABLE= models.CharField(max_length=250,blank=True, null=True, default=None)
    CATEGORY_TIMESTAMP= models.CharField(max_length=250,blank=True, null=True, default=None)
    CATEGORY_DURATION= models.CharField(max_length=250,blank=True, null=True, default=None)
    CATEGORY_RANGESTDAYS= models.CharField(max_length=250,blank=True, null=True, default=None)
    CATEGORY_RANGEENDDAYS= models.CharField(max_length=250,blank=True, null=True, default=None)


class ApiContextProvider(models.Model):
    PROVIDER_NAME= models.CharField(max_length=250)
    PROVIDER_CODE= models.CharField(max_length=250,blank=True, null=True, default=None,)
    PROVIDER_SYMBOL= models.CharField(max_length=250,blank=True, null=True, default=None,)
    PRODIVER_SHORTDESC= models.CharField(max_length=250,blank=True, null=True, default=None,)
    PROVIDER_LONGDESC= models.CharField(max_length=250,blank=True, null=True, default=None)
    PROVIDER_IMAGES= models.ImageField(upload_to='upload',blank=True, null=True, default=None)  
    PR0VIDER_TIMELABLE= models.CharField(max_length=250,blank=True, null=True, default=None)
    PROVIDER_TIMESTAMP= models.CharField(max_length=250,blank=True, null=True, default=None)
    PROVIDER_DURATION= models.CharField(max_length=250,blank=True, null=True, default=None)
    PROVIDER_RANGESTDAYS= models.CharField(max_length=250,blank=True, null=True, default=None)
    PROVIDER_RANGEENDAYS= models.CharField(max_length=250,blank=True, null=True, default=None)

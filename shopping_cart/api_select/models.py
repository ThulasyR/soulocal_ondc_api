from django.db import models

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

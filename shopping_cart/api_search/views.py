from django.shortcuts import render
#from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from .models import ApiContextModel
from .models import ApiContextCategory

# Create your views here.


@method_decorator(csrf_exempt, name='dispatch')
class CategoryView(View):

    def get(self, request):
        # items_count = ApiContextModel.objects.count() 
        contexts = ApiContextModel.objects.all()  
        catorgies = ApiContextCategory.objects.all() 

        context_data = {}
        for context in contexts:
            context_data={
                "domain": context.domain,
                "country": context.country,
                "city": context.city,
                "action": context.action,
                "core_version":  context.core_version,
                "bap_id":  context.bap_id,
                "bap_uri":  context.bap_uri,
                "bpp_id":  context.bpp_id,
                "bpp_uri": context.bpp_uri,
                "transaction_id":  context.transaction_id,
                "message_id":  context.message_id,
                "timestamp":  context.timestamp,
                "key":  context.key,
                "ttl":  context.ttl
                }

            category_names={}
            category_id={}
            for cat in catorgies:
                category_id={
					"id":cat.id, 
                }
                category_names={
                    "name":cat.CATEGORY_NAME,
                    "code":cat.CATEGORY_CODE,
                    "symbol":cat.CATEGORY_SYMBOL,
                    "short_desc":cat.CATEGORY_SHORTDESC,
                    "long_desc":cat.CATEGORY_LONGDESC, 
                }
            data = {
                'context': context_data,
                "message": {
        "intent" : {
            "category":
                {
                "descriptor" :  category_names 
            },
            "fulfillment": {
                "end" : {
                    "location" : {
                        "gps" : "12.4535445,77.9283792"
                    }
                }
            }
        }
    }
}
        return JsonResponse(data)
           




@method_decorator(csrf_exempt, name='dispatch')
class ItemsView(View):

    def get(self, request):
        # items_count = ApiContextModel.objects.count() 
        contexts = ApiContextModel.objects.all()  

        context_data = {}
        for context in contexts:
            context_data={
                "domain": context.domain,
                "country": context.country,
                "city": context.city,
                "action": context.action,
                "core_version":  context.core_version,
                "bap_id":  context.bap_id,
                "bap_uri":  context.bap_uri,
                "bpp_id":  context.bpp_id,
                "bpp_uri": context.bpp_uri,
                "transaction_id":  context.transaction_id,
                "message_id":  context.message_id,
                "timestamp":  context.timestamp,
                "key":  context.key,
                "ttl":  context.ttl
                }

            data = {
                'context': context_data,
                "message": {
        "intent" : {
            "item": {
                "descriptor" : {
                    "name" : "ABC Aata"
                }
            },
            "fulfillment": {
                "end" : {
                    "location" : {
                        "gps" : "12.4535445,77.9283792"
                    }
                }
            }
        }
    }
}
        return JsonResponse(data)
           
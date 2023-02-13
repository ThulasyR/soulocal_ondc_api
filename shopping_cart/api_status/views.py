from django.shortcuts import render
#from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from .models import ApiorderModel

@method_decorator(csrf_exempt, name='dispatch')
class status(View):

    def get(self, request):
        # items_count = ApiContextModel.objects.count() 
        contexts = ApiorderModel.objects.all()  
        data = {}
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
        "order": {
            
                "id": "453678",
                 
            }, 
    }
}
        return JsonResponse(data)
           
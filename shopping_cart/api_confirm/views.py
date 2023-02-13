from django.shortcuts import render
#from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from .models import ApiContextModel
from .models import ApiContextCategory
from .models import ApiContextProvider
from .models import ApiContextConfirm

@method_decorator(csrf_exempt, name='dispatch')
class confirm(View):

    def get(self, request):
        # items_count = ApiContextModel.objects.count() 
        contexts = ApiContextModel.objects.all()  
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
            "provider": {
                "id": "453678",
                "locations": [
                    {
                        "id": "el"
                    }
                ]
            },
            "items": [
                {
                    "id": "G-0007",
                    "quantity": {
                        "count": 1
                    }
                },
                {
                    "id": "G-0007-1",
                    "quantity": {
                        "count": 2
                    }
                }
            ],
        "billing": {
        "name": "string",
        "organization": {
          "name": "string",
          "cred": "string"
        },
        "address": {
          "door": "string",
          "name": "string",
          "building": "string",
          "street": "string",
          "locality": "string",
          "ward": "string",
          "city": "string",
          "state": "string",
          "country": "string",
          "area_code": "string"
        },
        "email": "user@example.com",
        "phone": "string",
        "time": {
          "label": "string",
          "timestamp": "2023-01-18T12:07:11.470Z",
          "duration": "string",
          "range": {
            "start": "2023-01-18T12:07:11.470Z",
            "end": "2023-01-18T12:07:11.470Z"
          },
          "days": "string",
          "schedule": {
            "frequency": "string",
            "holidays": [
              "2023-01-18T12:07:11.470Z"
            ],
            "times": [
              "2023-01-18T12:07:11.470Z"
            ]
          }
        }
        }
        }
    }
}
        return JsonResponse(data)
           
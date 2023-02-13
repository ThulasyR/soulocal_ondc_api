from django.shortcuts import render
# from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from .models import ApiContextModel
from .models import ApiContextCategory
from .models import ApiContextProvider
from .models import ApiContextConfirm

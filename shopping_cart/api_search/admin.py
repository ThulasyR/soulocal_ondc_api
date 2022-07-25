from django.contrib import admin

from .models import ApiContextModel
from .models import ApiContextCategory

admin.site.register(ApiContextModel)
admin.site.register(ApiContextCategory)

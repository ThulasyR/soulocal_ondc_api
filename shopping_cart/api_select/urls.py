from django.urls import path
from .views import CategoryView, add_toview

urlpatterns = [
    path('ondc/search/categoryname', add_toview.as_view()),
]
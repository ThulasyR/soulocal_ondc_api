from django.urls import path
from .views import CategoryView,ItemsView

urlpatterns = [
    path('ondc/search/categoryname', CategoryView.as_view()),
    path('ondc/search/itemname', ItemsView.as_view()),
]

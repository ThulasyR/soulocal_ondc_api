from django.urls import path
from .views import SearchListView

urlpatterns = [
    path('ondc/search', SearchListView.as_view()),
    # path('ondc/search/itemname', ItemsView.as_view()),
    # path('ondc/search/providername', providerview.as_view()),
]

from django.urls import path
from .views import status

urlpatterns = [
    path('ondc/status', status.as_view()),
    # path('ondc/search/itemname', ItemsView.as_view()),
    # path('ondc/search/providername', providerview.as_view()),
]

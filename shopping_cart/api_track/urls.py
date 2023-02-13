from django.urls import path
from .views import track

urlpatterns = [
    path('ondc/track', track.as_view()),
    # path('ondc/search/itemname', ItemsView.as_view()),
    # path('ondc/search/providername', providerview.as_view()),
]

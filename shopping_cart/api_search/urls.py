from django.urls import path
from .views import SearchListView, init, confirm, add_toview, status,track

urlpatterns = [
    path('ondc/search', SearchListView.as_view()),
    path('ondc/init', init.as_view()),
    path('ondc/confirm', confirm.as_view()),
    path('ondc/search/categoryname', add_toview.as_view()),
    path('ondc/status', status.as_view()),
    path('ondc/track', track.as_view()),
    # path('ondc/search/itemname', ItemsView.as_view()),
    # path('ondc/search/providername', providerview.as_view()),
]

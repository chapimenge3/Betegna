from django.urls import  path

from .views import Homepage, ItemDetail

urlpatterns = [
    path('', Homepage.as_view(), name="index"),
    path('item/<int:pk>', ItemDetail.as_view(), name="item_detail")
]

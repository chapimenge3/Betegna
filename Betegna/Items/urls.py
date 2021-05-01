from django.urls import  path
from django.urls.conf import include
from .views import (
    Homepage, ItemDetail, CreateCheckoutSession, success_checkout, cancel_checkout,
    StripeWebhookView)

from rest_framework import routers

# router = routers.DefaultRouter()
# router.register('create-checkout-session/{item}/', CreateCheckoutSession)

urlpatterns = [
    
    path('', Homepage.as_view(), name="index"),
    # path('', include(router.urls)),
    path('item/<int:pk>', ItemDetail.as_view(), name="item_detail"),
    path('create-checkout-session/<int:item>/', CreateCheckoutSession, name="create-session" ),
    path('success-checkout/', success_checkout, name="success-checkout" ),
    path('cancel-checkout/', cancel_checkout, name="cancel-checkout" ),
    path('stripe-webhook', StripeWebhookView.as_view(), name="stripe-webhook" ),
]

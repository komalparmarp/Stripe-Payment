from django.urls import path
from .views import *

urlpatterns = [
    path('cancel.html', CancelView.as_view(), name='cancel-view'),
    path('success', SuccessView.as_view(), name='success-view'),
    path('create-checkout-session/<pk>/', CreateCheckOutSessionView.as_view(), name='create-checkout-session'),
    path('', ProductLandingPagView.as_view(), name='product-template'),
    path('create-payment-intent/<pk>', StripeIntentView.as_view(), name='stripe-intent'),


    path('webhook/stripe', stripe_webhook, name='webhook-stripe'),

]

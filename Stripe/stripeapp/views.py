from django.shortcuts import render
from rest_framework.views import View, APIView
import stripe
from django.conf import settings
from django.http import JsonResponse
from django.views.generic import TemplateView
from .models import *
from django.http import HttpResponseRedirect

stripe.api_key = settings.STRIPE_SECRET_KEY


# Create your views here.
class SuccessView(TemplateView):
    template_name = "success.html"


class CancelView(TemplateView):
    template_name = "cancel.html"


class ProductLandingPagView(TemplateView):
    template_name = "landing.html"

    def get_context_data(self, **kwargs):
        product = Product.objects.get(name='TestProduct')
        context = super(ProductLandingPagView, self).get_context_data(**kwargs)
        context.update({"product": product,
                        "STRIPE_PUBLISHABLE_KEY": settings.STRIPE_PUBLISHABLE_KEY
                        })
        return context


class CreateCheckOutSessionView(View):
    def post(self, request, *args, **kwargs):
        product = Product.objects.get(id=self.kwargs['pk'])
        print(product)
        YOUR_DOMAIN = "http://127.0.0.1:8000"
        checkout_session = stripe.checkout.Session.create(
            # payment_method_type=['card'],
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price_data': {'currency': 'usd',
                                   'unit_amount': product.price,
                                   'product_data': {'name': product.name}},
                    # 'price': product.price,
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success',
            cancel_url=YOUR_DOMAIN + '/cancel',
        )
        return JsonResponse({'id': checkout_session.id})
        # return HttpResponsseRedirect(checkout_session.id)

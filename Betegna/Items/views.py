import random
from django.shortcuts import render, reverse
from django.http import JsonResponse, HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView, DetailView

from rest_framework.views import APIView
from rest_framework.response import Response


import stripe

from .models import Category, Item


class Homepage(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        filter = request.GET["filter"] if "filter" in request.GET else ""
        # print("Filter is ", filter)
        categories = Category.objects.all()
        items = (
            Item.objects.all()
            if not filter
            else Item.objects.filter(category__category__icontains=filter)
        )
        stars = [("★" * i.stars) + ("☆" * abs(i.stars - 5)) for i in items]
        itemlist = [{"item": i, "star": j} for i, j in zip(items, stars)]
        # print(showcase)
        context = {
            "items": items,
            "categories": categories,
            "stars": stars,
            "itemlist": itemlist,
        }
        # print(stars)

        return render(request, self.template_name, context)


class ItemDetail(DetailView):
    queryset = Item.objects.all()
    template_name = "item.html"
    context_object_name = "item"

    def get_context_data(self, **kwargs):
        kwargs["stripe_pub_key"] = settings.STRIPE_PUB_KEY
        return super().get_context_data(**kwargs)


@require_POST
@csrf_exempt
def CreateCheckoutSession(request, item):
    
    try:
        item = Item.objects.get(id=item)
        stripe.api_key = settings.STRIPE_SECRET_KEY
        success_url = (
            request.build_absolute_uri(reverse("success-checkout"))
            + "?session_id={CHECKOUT_SESSION_ID}"
        )
        cancel_url = request.build_absolute_uri(reverse("cancel-checkout"))
        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    "price_data": {
                        "currency": "usd",
                        "product_data": {
                            "name": item.name,
                        },
                        "unit_amount": int(item.price) * 100,
                    },
                    "quantity": 1,
                }
            ],
            mode="payment",
            success_url=success_url,
            cancel_url=cancel_url,
        )
        return JsonResponse({"id": session.id})
    except Exception as e:
        import traceback
        traceback.print_exc()
        return JsonResponse({"error": "invalid item id"}, status=404)
        # pass


def success_checkout(request):

    return HttpResponse(
        """<html>
<head>
  <title>Thanks for your order!</title>
</head>
<body>
  <section>
    <p>
      We appreciate your business! If you have any questions, please email
      <a href="mailto:orders@example.com">orders@example.com</a>.
    </p>
  </section>
</body>
</html>"""
    )


def cancel_checkout(request):
    return HttpResponse(
        """<html>

<head>

  <title>Checkout canceled</title>


</head>

<body>

  <section>

    <p>Forgot to add something to your cart? Shop around then come back to pay!</p>

  </section>

</body>

</html>"""
    )

class StripeWebhookView(APIView):
    http_method_names = ['post']
    

    def post(self, request):
        print("*"*10)
        print("Webhook called")
        print("*"*10)
        data = {}
        print(request.data)
        for i in request.data:
            print(type(i), i)
        print("here we go ")
        return Response({})
    
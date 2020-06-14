from django.shortcuts import render
from django.views import View

# Create your views here.

class Deshboard(View):
    def get(self, request):
        try:
            return render(request, 'restaurant/payment.html')
        except Exception as error:
            pass

class Order(View):
    def post(self, request):
        try:
            return render(request, 'restaurant/ongoing_payment.html')
        except Exception as error:
            pass
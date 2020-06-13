from django.shortcuts import render
from django.views import View

# Create your views here.

class Deshboard(View):
    def get(self, request):
        try:
            return render(request, 'restaurant/deshboard.html')
        except Exception as error:
            pass
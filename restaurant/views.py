from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from . import Checksum
from django.http import HttpResponse
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
            MERCHANT_KEY = '**********'
            data_dict = {
            'MID':'merchantId',
            'ORDER_ID':'dddgfgfeeee',
            'TXN_AMOUNT':'1',
            'CUST_ID':'adityasingh931@gmail.com',
            'INDUSTRY_TYPE_ID':'Retail',
            'WEBSITE':'WEBSTAGING',
            'CHANNEL_ID':'WEB',
	        'CALLBACK_URL':'http://localhost:8000/api/deshboard/handlerequest/',
        }
            param_dict = data_dict  
            param_dict['CHECKSUMHASH'] =Checksum.generate_checksum(data_dict, MERCHANT_KEY)
            return render(request, 'restaurant/ongoing_payment.html', {'param_dict': param_dict})
        except Exception as error:
            pass

@csrf_exempt #gives freedom of csrf
def handlerequest(request):
    #patym will send you post request here
    MERCHANT_KEY = '*********'
    form = request.POST
    reponse_dict = {}
    for i in form.keys():
        reponse_dict[i] = form[i]
        if i =='CHECKSUMHASH':
            checksum = form[i]
    verify = Checksum.verify_checksum(reponse_dict, MERCHANT_KEY, checksum)
    if verify:
        if reponse_dict['RESPCODE'] == '01':
            print("successsful")
        else:
            print("failed"+ reponse_dict['RESPMSG'])

    return HttpResponse("thank you")
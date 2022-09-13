from django.shortcuts import render, HttpResponse, Http404, get_object_or_404
from frontend.models import *
from .models import *
# Create your views here.

import logging
from django.urls import reverse
from azbankgateways import bankfactories, models as bank_models, default_settings as settings
from azbankgateways.exceptions import AZBankGatewaysException


def go_to_gateway_view(request):
    if request.user.is_authenticated:
        cart = Cart.objects.get(user=request.user)
        amount=sum([pro.price for pro in cart.pids.filter(status="published")])
        
        factory = bankfactories.BankFactory()
        try:
            bank = factory.create() # or factory.create(bank_models.BankType.BMI) or set identifier
            bank.set_request(request)
            bank.set_amount(amount*10)
            # یو آر ال بازگشت به نرم افزار برای ادامه فرآیند
            bank.set_client_callback_url(f'/callback-gateway/{request.user.id}/{int(amount*10)}/')
        
            # در صورت تمایل اتصال این رکورد به رکورد فاکتور یا هر چیزی که بعدا بتوانید ارتباط بین محصول یا خدمات را با این
            # پرداخت برقرار کنید. 
            bank_record = bank.ready()
            
            # هدایت کاربر به درگاه بانک
            return bank.redirect_gateway()
        except AZBankGatewaysException as e:
            logging.critical(e)
            # TODO: redirect to failed page.
            raise e
    else:
        print("12*%&*^*&^&*^^^&^&^&$################")
        raise Http404

#=========================================


def callback_gateway_view(request, userid, amount):
    tracking_code = request.GET.get(settings.TRACKING_CODE_QUERY_PARAM, None)
    if not tracking_code:
        logging.debug("این لینک معتبر نیست.")
        print("23*%&*^*&^&*^^^&^&^&$################")
        raise Http404

    try:
        bank_record = bank_models.Bank.objects.get(tracking_code=tracking_code)
    except bank_models.Bank.DoesNotExist:
        logging.debug("این لینک معتبر نیست.")
        print("34*%&*^*&^&*^^^&^&^&$################")
        raise Http404

    # در این قسمت باید از طریق داده هایی که در بانک رکورد وجود دارد، رکورد متناظر یا هر اقدام مقتضی دیگر را انجام دهیم
    if bank_record.is_success:
        user = get_object_or_404(User, id=userid)
        g = gateway_check(amount=int(amount),user=user,payment_status=True,tracking_code=tracking_code)
        g.save()
        cart = Cart.objects.get(user=user)
        cart.delete()
        cart.save()
            # پرداخت با موفقیت انجام پذیرفته است و بانک تایید کرده است.
            # می توانید کاربر را به صفحه نتیجه هدایت کنید یا نتیجه را نمایش دهید.
        return render(request, 'peyments/success.html')



    
    try:
        user = get_object_or_404(User, id=userid)
        g = gateway_check(amount=int(amount),user=user,payment_status=False,tracking_code=tracking_code)
        g.save()
    
        # پرداخت موفق نبوده است. اگر پول کم شده است ظرف مدت ۴۸ ساعت پول به حساب شما بازخواهد گشت.
        return render(request, 'peyments/failed.html')
    except:
        print("1572*%&*^*&^&*^^^&^&^&$################")
        raise Http404

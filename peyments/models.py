from django.db import models
from django.utils import timezone
from frontend.models import User

# Create your models here.

class gateway_check(models.Model):
	id = models.AutoField(primary_key=True)
	user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, verbose_name="کاربر")
	amount = models.IntegerField(verbose_name="مبلغ", default=0)
	date = models.DateTimeField(default=timezone.now, verbose_name="تاریخ و زمان")
	payment_status = models.BooleanField(default=False, verbose_name="وضعیت پرداخت")
	tracking_code = models.IntegerField(unique=True,verbose_name="کد پیگیری")

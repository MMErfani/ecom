from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.

class User(AbstractUser):
    phone = models.CharField(max_length=12, default='09123456789', verbose_name="شماره تلفن")
    avatar = models.ImageField(upload_to="avatars",verbose_name="آواتار", default='avatar.png')
    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"
        ordering = ['-is_superuser']
 
class Category(models.Model):
    title = models.CharField(max_length=250, verbose_name="عنوان")
    slug = models.SlugField(max_length=250, unique = True , verbose_name="آدرس")
    status = models.BooleanField(default=True, verbose_name="وضعیت نمایش")
    position = models.IntegerField(verbose_name="پوزیشن")

    class Meta():
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"
        ordering = ['position']


    
    def __str__(self):
        return self.title
               
class Product(models.Model):
    STATUS_CHOICES=(
        ('draft' , 'پیش نویس یا در انتظار تایید'),
        ('published', 'منتشر شده')
    )
    productname = models.CharField(max_length=200,verbose_name="نام محصول")
    price = models.DecimalField(max_digits=20, decimal_places=2,verbose_name="قیمت")
    description = models.CharField(max_length=1024, default="", verbose_name="توضیحات")
    image = models.ImageField(upload_to="uploads/images/", max_length=52428,default="img.png", verbose_name="تصویر")
    slug = models.SlugField(max_length=250, unique_for_date= "publish", verbose_name="آدرس")
    seller = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, verbose_name="فروشنده")
    category = models.ManyToManyField(Category, verbose_name="دسته بندی")
    body = models.TextField(verbose_name="متن")
    publish = models.DateTimeField(default=timezone.now, verbose_name="زمان انتشار")
    created = models.DateTimeField(auto_now_add=True, verbose_name="ساخته شده")
    updated = models.DateTimeField(auto_now=True, verbose_name="بروز شده")
    upload = models.FileField(upload_to ='uploads/files/', max_length=524288,verbose_name="فایل")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft", verbose_name="وضعیت")
    pid = models.AutoField(primary_key=True)
    class Meta():
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"

    
    def __str__(self):
        return self.productname
        

class Cart(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, verbose_name="کاربر")
    pids = models.ManyToManyField(Product,blank=True, verbose_name="محصولات")
    position = models.IntegerField(default=1, verbose_name="پوزیشن")
    class Meta():
        verbose_name = "سبد خرید"
        verbose_name_plural = "سبدهای خرید"

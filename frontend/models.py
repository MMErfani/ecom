from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass

    def __str__(self):
        return self.username
 
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
    productname = models.CharField(max_length=200,verbose_name="نام محصول")
    price = models.DecimalField(max_digits=20, decimal_places=2,verbose_name="قیمت")
    description = models.TextField(max_length=500000,verbose_name="توضیحات")
    image = models.ImageField(upload_to="uploads/images/", max_length=52428,default="img.png", verbose_name="تصویر") #, default='avatar.png')
    upload = models.FileField(upload_to ='uploads/files/', max_length=524288,verbose_name="فایل")

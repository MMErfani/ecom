from django.urls import path
from .views import Profile

app_name = "accounts"

urlpatterns = [
    path('', Profile.as_view(), name='Profile'),
]

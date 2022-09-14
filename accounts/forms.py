from django import forms
from django.contrib.auth.forms import UserCreationForm
from frontend.models import User

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

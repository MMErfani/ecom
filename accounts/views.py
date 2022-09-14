from django.shortcuts import render
#from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from frontend.models import User
from django.views.generic import UpdateView,CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordChangeView

# Create your views here.
    
class Profile(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'username', 'email', 'phone','avatar',]
    template_name = 'registration/home.html'
    success_url = reverse_lazy('accounts:Profile')
    
    def get_object(self):
        return User.objects.get(pk = self.request.user.pk)


from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from frontend.models import User
from django.core.mail import EmailMessage

class Register(CreateView):
    form_class = SignupForm
    template_name = 'registration/register.html'
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        current_site = get_current_site(self.request)
        mail_subject = 'فعال سازی اکانت'
        message = render_to_string('registration/activate_account.html', {
            'user': user,
            'domain': current_site.domain,
            'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            'token':account_activation_token.make_token(user),
        })
        to_email = form.cleaned_data.get('email')
        email = EmailMessage(mail_subject, message, to=[to_email])
        email.send()
        return redirect("/register/done/")
        
def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return redirect("/account/")
    else:
        return redirect("/register/failed/")# HttpResponse('این لینک منقضی شده است!<a href="/register/">دوباره امتحان کنید.</a>')
def registerdone(request):
	return render(request, 'registration/registerdone.html')

def registerfailed(request):
	return render(request, 'registration/registerfailed.html')

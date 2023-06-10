from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


from .forms import RegistrationForm, LoginForm
from django.views.generic import CreateView
from .models import DeliveryUser


class UserLoginView(LoginView):
    template_name = 'userapp/login.html'
    authentication_form = LoginForm


class UserCreateView(CreateView):
    model = DeliveryUser
    template_name = 'userapp/registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('userapp:login')

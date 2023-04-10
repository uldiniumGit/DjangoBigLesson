from django.contrib.auth.forms import UserCreationForm
from .models import DeliveryUser


class RegistrationForm(UserCreationForm):
    class Meta:
        model = DeliveryUser
        fields = ('username', 'password1', 'password2', 'email')

from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import Users, NewUser
class NewUserForm(UserCreationForm):
    class Meta:
        model = NewUser
        fields = [
            'id',
            'password',
        ]

class CustomUserUpdate(UserChangeForm):
    password = None
    class Meta:
        model = get_user_model()
        fields = [
            'first_name',
            'last_name',
            'email',
        ]

class CustumUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ()
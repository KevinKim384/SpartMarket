from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model
from .models import Users

class NewUserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = '__all__'
        exclude = ('username',)

class CustumUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ()
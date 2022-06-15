from .models import ProfileModel
from django.contrib.auth.forms import UserCreationForm, forms
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2', )


class ProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        exclude = ('user',)

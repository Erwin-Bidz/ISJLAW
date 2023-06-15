from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#create our forms here

class UserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
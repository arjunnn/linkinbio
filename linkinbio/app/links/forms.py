from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


class SignUpForm(forms.Form):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={"class": "input", "placeholder": "email"}),
    )
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "input", "placeholder": "username"}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "input", "placeholder": "password"}),
        required=True,
    )


class SignInForm(forms.Form):
    username_or_email = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "input", "placeholder": "username or email"}
        ),
        required=True,
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "input", "placeholder": "password"}),
        required=True,
    )

    def __init__(self, *args, **kwargs):
        super(SignInForm, self).__init__(*args, **kwargs)
        self.user = None

    def clean(self):
        username_or_email = self.cleaned_data.get("username_or_email")
        username = None
        email = None
        password = self.cleaned_data.get("password")
        try:
            validate_email(username_or_email)
            email = username_or_email
        except ValidationError:
            username = username_or_email
        if email and not username:
            try:
                username = get_user_model().objects.get(email=email).username
            except get_user_model().DoesNotExist:
                raise forms.ValidationError(f"User with email {email} does not exist")
        self.user = authenticate(request=None, username=username, password=password)
        if not self.user:
            raise forms.ValidationError(f"Login failed. Please try again")

from django import forms


class SignUpForm(forms.Form):
    email = forms.EmailField()
    username = forms.CharField()
    password = forms.PasswordInput()

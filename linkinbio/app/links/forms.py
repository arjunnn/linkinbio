from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

from ..links.models import Profile, ProfileTheme, Link


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


class EditProfileForm(forms.ModelForm):
    theme = forms.ModelChoiceField(
        queryset=ProfileTheme.objects.all().order_by("name"),
        widget=forms.Select(attrs={"class": "select select-bordered w-full"}),
        required=False,
    )
    bio = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "textarea h-24 textarea-bordered textarea-primary w-full"}
        ),
        required=False,
    )
    image = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={"class": "input w-full"}), required=False
    )
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "input input-bordered input-primary w-full"}
        ),
        required=False,
    )

    class Meta:
        model = Profile
        fields = ["bio", "image", "theme"]

    def __init__(self, *args, **kwargs):
        self.instance = kwargs.get("instance")
        if self.instance:
            self.base_fields["name"].initial = self.instance.user.first_name
        super(EditProfileForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        super(EditProfileForm, self).save(*args, **kwargs)
        name = self.cleaned_data.get("name")
        if name:
            self.instance.user.first_name = name
            self.instance.user.save()


class LinkForm(forms.ModelForm):
    link = forms.URLField(widget=forms.URLInput(attrs={"class": "input truncate"}))
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "input"}))
    id = forms.IntegerField(widget=forms.HiddenInput)

    class Meta:
        model = Link
        fields = ["link", "name", "id"]

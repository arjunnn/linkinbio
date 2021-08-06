from django.shortcuts import redirect
from django import forms
from django.contrib import messages
from django.contrib.auth import get_user_model, login, logout
from django.forms import modelformset_factory
from django.http.response import (
    HttpResponseNotFound,
    HttpResponseBadRequest,
    HttpResponse,
)
from django.shortcuts import redirect
from django.shortcuts import reverse
from django.template.response import TemplateResponse, SimpleTemplateResponse
from django.views import View

from .forms import SignUpForm, SignInForm, EditProfileForm
from ..links.models import Profile, Link


class ProfileView(View):
    def get(self, request, *args, **kwargs):
        username = kwargs.get("username")
        iframe = True if request.GET.get("iframe") else False
        try:
            profile = Profile.objects.get(user__username=username)
            if not iframe:
                profile.hits += 1
                profile.save()
            response = SimpleTemplateResponse(
                "profile.html", {"profile": profile, "iframe": iframe}
            )
            return response
        except Exception as e:
            return HttpResponseNotFound()


class SignUpView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("edit-profile", username=request.user.username)
        username = kwargs.get("username")
        if username:
            if get_user_model().objects.filter(username=username).exists():
                return HttpResponse(status=409)
            else:
                return HttpResponse(status=204)
        form = SignUpForm(request.GET)
        response = TemplateResponse(request, "signup.html", context={"form": form})
        return response

    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)
        if form.is_valid():

            data = form.cleaned_data
            created_user = get_user_model().objects.create_user(
                username=data.get("username"),
                email=data.get("email"),
                password=data.get("password"),
            )
            login(request, user=created_user)
            profile = Profile.objects.create(user=created_user)
            messages.success(request, "Welcome! Get started by creating your profile.")
            return redirect("edit-profile", username=created_user.username)
        else:
            messages.error(request, "error", "Sign up failed. Please try again.")
            return redirect(reverse("signup"))


class LoginView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("edit-profile", request.user.username)
        response = TemplateResponse(
            request, "login.html", {"form": SignInForm(request.GET)}
        )
        return response

    def post(self, request, *args, **kwargs):
        form = SignInForm(request.POST)
        form.full_clean()
        if form.is_valid():
            login(request, form.user)
            messages.info(request, f"Welcome {form.user.username} 👋")
            return redirect("edit-profile", username=form.user.username)
        else:
            messages.error(request, f"😟 Login failed. Please try again")
            return redirect(reverse("login"))


class RedirectView(View):
    def get(self, request, *args, **kwargs):
        uuid = kwargs.get("uuid")
        if not uuid:
            return HttpResponseBadRequest()
        try:
            link = Link.objects.get(uuid=uuid)
            link.hits += 1
            link.save()
            return redirect(link.link)
        except (Link.DoesNotExist, ValueError) as e:
            raise e
            return HttpResponseNotFound()
        except Exception:
            return HttpResponseBadRequest()


class DashboardView(View):
    def __init__(self, **kwargs):
        self.profile: Profile = None
        self.LinkFormSet = None

    def setup(self, request, *args, **kwargs):
        super(DashboardView, self).setup(self, request, *args, **kwargs)
        if request.user.is_authenticated:
            self.profile = request.user.profile
        self.LinkFormSet = modelformset_factory(
            Link,
            fields=("id", "name", "link"),
            can_delete=True,
            extra=2,
            widgets={
                "id": forms.HiddenInput,
                "name": forms.TextInput(
                    attrs={
                        "class": "input input-bordered truncate mb-1 mr-1 flex-auto",
                        "placeholder": "description",
                    }
                ),
                "link": forms.TextInput(
                    attrs={
                        "class": "input input-bordered truncate ml-1",
                        "placeholder": "link",
                    }
                ),
            },
        )

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse("login"))
        link_formset = self.LinkFormSet()
        context = {
            "edit_profile_form": EditProfileForm(instance=self.profile),
            "link_formset": link_formset,
        }
        response = TemplateResponse(request, "edit_profile.html", context=context)
        return response

    def post(self, request, *args, **kwargs):
        link_formset = self.LinkFormSet(request.POST, request.FILES)
        edit_profile_form = EditProfileForm(
            request.POST, instance=self.profile, files=request.FILES
        )
        if edit_profile_form.is_valid():
            edit_profile_form.save()
        else:
            print(edit_profile_form.errors)
        if link_formset.is_valid():
            link_formset.save()
            for form in link_formset:
                instance = form.save(commit=False)
                if not (instance.name and instance.link):
                    continue
                if form.cleaned_data.get("DELETE"):
                    instance.delete()
                else:
                    instance.profile = request.user.profile
                    instance.save()
            messages.success(request, "Profile updated successfully ✨")
        else:
            print(link_formset.errors)
        return redirect("edit-profile", username=request.user.username)


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
        return redirect(reverse("login"))

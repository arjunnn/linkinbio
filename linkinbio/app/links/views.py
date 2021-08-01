from django.views import View
from django.shortcuts import redirect
from django.template.response import TemplateResponse, SimpleTemplateResponse
from django.http.response import (
    HttpResponseNotFound,
    HttpResponseBadRequest,
    HttpResponse,
)
from django.shortcuts import reverse
from django.views import View
from django.contrib import messages
from django.contrib.auth import get_user_model, login, logout

from .forms import SignUpForm, SignInForm
from ..links.models import Profile, Link
from django.contrib.auth.models import User


class ProfileView(View):
    def get(self, request, *args, **kwargs):
        username = kwargs.get("username")
        try:
            profile = Profile.objects.get(user__username=username)
            profile.hits += 1
            profile.save()
            response = SimpleTemplateResponse("profile.html", {"profile": profile})
            return response
        except Exception as e:
            return HttpResponseNotFound()


class SignUpView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse("dashboard"))
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
            messages.success(request, "Welcome! we've logged you in.")
            return redirect(reverse("dashboard"))
        else:
            messages.error(request, "error", "Sign up failed. Please try again.")
            return redirect(reverse("signup"))


class LoginView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse("dashboard"))
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
            return redirect("dashboard")
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
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse("login"))
        response = TemplateResponse(request, "dashboard.html")
        return response


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
        return redirect(reverse("login"))

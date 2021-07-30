from django.views import View
from django.shortcuts import redirect
from django.template.response import TemplateResponse, SimpleTemplateResponse
from django.views import View

from .forms import SignUpForm
from ..links.models import Profile, Link


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
        form = SignUpForm()
        response = TemplateResponse(request, "signup.html", context={"form": form})
        return response


class LoginView(View):
    def get(self, request, *args, **kwargs):
        response = SimpleTemplateResponse("login.html")
        return response


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
        except (Link.DoesNotExist, ValueError):
            return HttpResponseNotFound()
        except Exception:
            return HttpResponseBadRequest()

from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, Http404
from django.template.response import TemplateResponse, SimpleTemplateResponse

from ..links.models import Profile

# Create your views here.


class ProfileView(View):
    def get(self, request, *args, **kwargs):
        print(args, kwargs)
        username = kwargs.get("username")
        try:
            profile = Profile.objects.get(user__username=username)
        except Exception as e:
            print(e)
            return HttpResponse(status=404)
        if profile:
            response = SimpleTemplateResponse("profile.html", {"profile": profile})
            return response

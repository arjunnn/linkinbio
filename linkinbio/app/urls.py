"""linkinbio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .api.urls import urlpatterns as api_url_patterns
from .links.views import (
    ProfileView,
    SignUpView,
    LoginView,
    RedirectView,
    DashboardView,
    LogoutView,
    StatsView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "api/",
        include(api_url_patterns),
    ),
    path("<username>/", ProfileView.as_view(), name="profile"),
    path("<username>/edit", DashboardView.as_view(), name="edit-profile"),
    path("signup", SignUpView.as_view(), name="signup"),
    path("signup/check/<username>", SignUpView.as_view(), name="check_availability"),
    path("login", LoginView.as_view(), name="login"),
    path("logout", LogoutView.as_view(), name="logout"),
    path("", SignUpView.as_view(), name="home"),
    path("dashboard", DashboardView.as_view(), name="dashboard"),
    path("r/<uuid>", RedirectView.as_view(), name="redirect"),
    path("stats", StatsView.as_view(), name="stats"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

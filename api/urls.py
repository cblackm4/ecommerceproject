"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from .router import ROUTER
from administration.views import SignUp, EmailVerified, verify_email
from administration import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",
        TemplateView.as_view(template_name="application.html"),
        name="app",
    ),
    path('accounts/', include('django.contrib.auth.urls')),
    path(r'accounts/signup/', SignUp.as_view(), name='signup'),
    path('verify_email/<uuid:token>/', verify_email, name='verify_email'),
    path('email_verified/', EmailVerified.as_view(), name='email_verified'),
    path('api/', include(ROUTER.urls)),
]

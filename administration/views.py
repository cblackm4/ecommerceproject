from django.contrib.auth.models import Group
from .forms import UserCreateForm
from django.urls import reverse, reverse_lazy
from django.views import generic
from rest_framework import viewsets
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .models import User, EmailVerificationToken
from .serializers import UserSerializer, GroupSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class SignUp(generic.CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class EmailVerified(generic.TemplateView):
    template_name = 'email/email_verified.html'

def verify_email(request, token):
    try:
        verif = EmailVerificationToken.objects.get(token=token)
        verif.user.email = verif.email
        verif.user.save()
        verif.delete()
        return HttpResponseRedirect(reverse('email_verified'))
    except Exception:
        return HttpResponseRedirect(reverse('login'))

from django.contrib.auth.models import Group
from .forms import UserCreateForm
from django.urls import reverse_lazy
from django.views import generic
from rest_framework import viewsets
from django.http import HttpResponse

from .models import User
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

def user_get(request):
    """
    Retrieve the information for the currently logged in user
    """
    if request.method == 'GET':
        serializer = UserSerializer(request.user,context={'request': request})

        return HttpResponse(request.user.username + '|' +
                           request.user.first_name + '|' +
                           request.user.last_name + '|' +
                           request.user.email + '|' +
                           request.user.password + '|')
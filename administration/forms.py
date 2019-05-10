from django import forms
from .models import User
from pawkages.models import Customer
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
    first_name = forms.CharField(max_length=64)
    last_name = forms.CharField(max_length=64)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            Customer.objects.create(user=user)
        return user

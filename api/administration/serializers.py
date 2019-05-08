from rest_framework import serializers
from django.core.mail import EmailMessage
from django.urls import reverse
from django.template.loader import get_template
from django.conf import settings
from django.contrib.auth.models import Group
from .models import User, EmailVerificationToken

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'is_staff')

    def update(self, instance, validated_data):
        request = self.context['request']
        new_email = validated_data.pop('email')
        if instance.email != new_email: # The email is being changed
            # Send email to old address warning of email change
            subject = 'Email Change Requested'
            to = [instance.email]
            ctx = {
                'first_name': validated_data.get('first_name')
            }
            message = get_template('email/change_notification.html').render(ctx)
            email = EmailMessage(subject, message, to=to, from_email=settings.EMAIL_HOST_USER)
            email.content_subtype = 'html'
            email.send()
            # Send email to new address with verification link
            subject = 'Email Verification'
            to = [new_email]
            token = EmailVerificationToken(user=request.user, email=new_email)
            token.save()
            ctx = {
                'first_name': validated_data.get('first_name'),
                'link': request.build_absolute_uri(reverse('verify_email', kwargs={'token' : token.token})),
            }
            message = get_template('email/change_link.html').render(ctx)
            email = EmailMessage(subject, message, to=to, from_email=settings.EMAIL_HOST_USER)
            email.content_subtype = 'html'
            email.send()
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__' # TODO restrict field visibility

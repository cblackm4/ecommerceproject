import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

class EmailVerificationToken(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    token = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField()


class User(AbstractUser):
    """
    Extension of Django's default User mode.
    """
    pass

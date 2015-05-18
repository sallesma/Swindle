from django.db import models
from django.contrib.auth.models import User


class TestPassword(models.Model):
    user = models.OneToOneField(User)
    test_password = models.CharField(max_length=200)

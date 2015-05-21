from django.db import models
from django.contrib.auth.models import User


class TestPassword(models.Model):
    user = models.OneToOneField(User)
    test_password = models.CharField(max_length=200)

class AuthTests(models.Model):
    user = models.OneToOneField(User)
    swindle_auth = models.NullBooleanField(default=None)
    github_auth = models.NullBooleanField(default=None)
    trello_auth = models.NullBooleanField(default=None)

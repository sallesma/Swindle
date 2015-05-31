from django.db import models
from django.contrib.auth.models import User


class TestData(models.Model):
    user = models.OneToOneField(User)
    password = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

class AuthTests(models.Model):
    user = models.OneToOneField(User)
    swindle_auth = models.NullBooleanField(default=None)
    github_auth = models.NullBooleanField(default=None)
    trello_auth = models.NullBooleanField(default=None)
    linkedin_auth = models.NullBooleanField(default=None)
    facebook_auth = models.NullBooleanField(default=None)

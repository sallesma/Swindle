from django.db import models
from django.contrib.auth.models import User

class TestPassword(models.Model):
    user = models.OneToOneField(User)
    test_password = models.CharField(max_length=200)


class Host(models.Model):
    name = models.CharField(max_length=200)
    connection_url = models.CharField(max_length=200)
    success_regexp = models.CharField(max_length=200)
    failure_regexp = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class SwindleTest(models.Model):
    user = models.ForeignKey(User)
    host = models.ForeignKey(Host)
    result = models.BooleanField(default=None)

    def __unicode__(self):
        return "Result for user %s and host %s : %s" % (self.user, self.host, self.result)



class HostParameter(models.Model):
    host = models.ForeignKey(Host)
    key = models.CharField(max_length=200)
    value = models.CharField(max_length=200)

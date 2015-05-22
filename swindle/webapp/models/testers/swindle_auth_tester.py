from django.contrib.auth import authenticate
import logging

logger = logging.getLogger("swindle")


class SwindleAuthTester(object):
    """Should always return true"""
    def can_auth(self, user):
        user = authenticate(username=user.testdata.username, password=user.testdata.password)
        if user is None:
            return False
        else:
            return True

from django.contrib.auth import authenticate
import logging

logger = logging.getLogger("swindle")


class SwindleAuthTester(object):
    """Should always return true"""
    def can_auth(self, user):
        user = authenticate(username=user.username, password=user.testpassword.test_password)
        if user is None:
            return False
        else:
            return True

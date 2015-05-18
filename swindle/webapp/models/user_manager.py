from django.contrib.auth.models import User
from django.db import IntegrityError
from webapp.models import TestPassword, AuthTests
from webapp.models import AuthTestManager
import logging

logger = logging.getLogger("swindle")


class UserManager:
    def create_user(self, first_name, last_name, username, email, password):
        try:
            user = User.objects.create_user(username, email, password)
        except IntegrityError:
            logger.error("Could not create user : username=%s, email=%s" % (username, email))
            return False

        user.first_name=first_name
        user.last_name=last_name
        user.save()

        test_password = TestPassword(user=user, test_password=password)
        test_password.save()
        auth_tests = AuthTests(user=user)
        auth_tests.save()

        manager = AuthTestManager()
        manager.test_auth(user)
        return True
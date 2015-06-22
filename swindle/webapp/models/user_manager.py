from django.contrib.auth.models import User
from django.db import IntegrityError
from webapp.models import TestData, AuthTests
from webapp.models import AuthTestManager
import logging

logger = logging.getLogger("swindle")


class UserManager:
    def create(self, first_name, last_name, username, email, password):
        try:
            user = User.objects.create_user(username, email, password)
        except IntegrityError:
            logger.info("Could not create user : username=%s, email=%s" % (username, email))
            return False

        user.first_name=first_name
        user.last_name=last_name
        user.save()

        test_data = TestData(user=user, password=password, username=username, email=email)
        test_data.save()
        auth_tests = AuthTests(user=user)
        auth_tests.save()

        AuthTestManager().test_all(user)
        return True

    def refresh(self, user, service):
        func = getattr(AuthTestManager, "test_%s" % service, None)
        if func:
            func(AuthTestManager(), user)

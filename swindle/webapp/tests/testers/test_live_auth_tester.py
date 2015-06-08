from django.test import TestCase
from django.contrib.auth.models import User
from webapp.models.testers import LiveAuthTester


class LiveAuthTesterTest(TestCase):
    fixtures = ['users', 'users_valid']

    def test_fake_user(self):
        """
        Should return false for a fake user
        """
        user = User.objects.get(username="a")

        tester = LiveAuthTester()
        self.assertFalse(tester.can_auth(user))


    def test_valid_live_user(self):
        """
        Should return false for a valid Live user
        """
        user = User.objects.get(id=109)

        tester = LiveAuthTester()
        self.assertTrue(tester.can_auth(user))


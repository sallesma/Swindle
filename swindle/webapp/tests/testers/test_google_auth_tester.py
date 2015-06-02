from django.test import TestCase
from django.contrib.auth.models import User
from webapp.models.testers import GoogleAuthTester


class GoogleAuthTesterTest(TestCase):
    fixtures = ['users', 'users_valid']

    def test_fake_user(self):
        """
        Should return false for a fake user
        """
        user = User.objects.get(username="a")

        tester = GoogleAuthTester()
        self.assertFalse(tester.can_auth(user))


    def test_valid_google_user(self):
        """
        Should return false for a valid google user
        """
        user = User.objects.get(id=106)

        tester = GoogleAuthTester()
        self.assertTrue(tester.can_auth(user))


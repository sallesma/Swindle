from django.test import TestCase
from django.contrib.auth.models import User
from webapp.models.testers import FacebookAuthTester


class FacebookAuthTesterTest(TestCase):
    fixtures = ['users', 'users_valid']

    def test_fake_user(self):
        """
        Should return false for a fake user
        """
        user = User.objects.get(username="a")

        tester = FacebookAuthTester()
        self.assertFalse(tester.can_auth(user))


    def test_valid_facebook_user(self):
        """
        Should return false for a valid facebook user
        """
        user = User.objects.get(id=104)

        tester = FacebookAuthTester()
        self.assertTrue(tester.can_auth(user))


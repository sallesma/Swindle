from django.test import TestCase
from django.contrib.auth.models import User
from webapp.models.testers import YahooAuthTester


class YahooAuthTesterTest(TestCase):
    fixtures = ['users', 'users_valid']

    def test_fake_user(self):
        """
        Should return false for a fake user
        """
        user = User.objects.get(username="a")

        tester = YahooAuthTester()
        self.assertFalse(tester.can_auth(user))


    def test_valid_yahoo_user(self):
        """
        Should return false for a valid yahoo user
        """
        user = User.objects.get(id=108)

        tester = YahooAuthTester()
        self.assertTrue(tester.can_auth(user))


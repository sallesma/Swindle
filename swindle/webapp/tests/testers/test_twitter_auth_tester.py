from django.test import TestCase
from django.contrib.auth.models import User
from webapp.models.testers import TwitterAuthTester


class TwitterAuthTesterTest(TestCase):
    fixtures = ['users', 'users_valid']

    def test_fake_user(self):
        """
        Should return false for a fake user
        """
        user = User.objects.get(username="a")

        tester = TwitterAuthTester()
        self.assertFalse(tester.can_auth(user))


#    def test_valid_twitter_user(self):
#        """
#        Should return true for a valid twitter user
#        """
#        user = User.objects.get(id=105)
#
#        tester = TwitterAuthTester()
#        self.assertTrue(tester.can_auth(user))


from django.test import TestCase
from django.contrib.auth.models import User
from webapp.models.testers import GithubAuthTester


class GithubAuthTesterTest(TestCase):
    fixtures = ['users', 'users_valid']

    def test_fake_user(self):
        """
        Should return false for a fake user
        """
        user = User.objects.get(username="a")

        tester = GithubAuthTester()
        self.assertFalse(tester.can_auth(user))


    def test_valid_github_user(self):
        """
        Should return false for a valid github user
        """
        user = User.objects.get(id=101)

        tester = GithubAuthTester()
        self.assertTrue(tester.can_auth(user))


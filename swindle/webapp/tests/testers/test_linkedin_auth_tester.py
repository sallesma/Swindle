from django.test import TestCase
from django.contrib.auth.models import User
from webapp.models import UserManager
from webapp.models import TestPassword
from webapp.models.testers import LinkedinAuthTester


class LinkedinAuthTesterTest(TestCase):
    fixtures = ['users', 'users_valid']

    def test_fake_user(self):
        """
        Should return false for a fake user
        """
        user = User.objects.get(username="a")

        tester = LinkedinAuthTester()
        self.assertFalse(tester.can_auth(user))


    def test_valid_linkedin_user(self):
        """
        Should return false for a valid linkedin user
        """
        user = User.objects.get(id=102)

        tester = LinkedinAuthTester()
        self.assertTrue(tester.can_auth(user))


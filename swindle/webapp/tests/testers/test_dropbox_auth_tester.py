from django.test import TestCase
from django.contrib.auth.models import User
from webapp.models.testers import DropboxAuthTester


class DropboxAuthTesterTest(TestCase):
    fixtures = ['users', 'users_valid']

    def test_fake_user(self):
        """
        Should return false for a fake user
        """
        user = User.objects.get(username="a")

        tester = DropboxAuthTester()
        self.assertFalse(tester.can_auth(user))


    def test_valid_dropbox_user(self):
        """
        Should return false for a valid dropbox user
        """
        user = User.objects.get(id=107)

        tester = DropboxAuthTester()
        self.assertTrue(tester.can_auth(user))


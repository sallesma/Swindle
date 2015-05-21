from django.test import TestCase
from django.contrib.auth.models import User
from webapp.models import UserManager
from webapp.models import TestPassword
from webapp.models.testers import TrelloAuthTester

# Create your tests here.
class TrelloAuthTesterTest(TestCase):
    fixtures = ['users', 'users_valid']

    def test_fake_user(self):
        """
        Should return false for a fake user
        """
        user = User.objects.get(username="a")

        tester = TrelloAuthTester()
        self.assertFalse(tester.can_auth(user))


    def test_valid_trello_user(self):
        """
        Should return false for a valid trello user
        """
        user = User.objects.get(id=101)

        tester = TrelloAuthTester()
        self.assertTrue(tester.can_auth(user))


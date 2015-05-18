from django.test import TestCase
from django.contrib.auth.models import User
from webapp.models import UserManager
from webapp.models import TestPassword
from webapp.models.testers import SwindleAuthTester

# Create your tests here.
class SwindleAuthTesterTest(TestCase):

    def test_registered_user(self):
        """
        Should return true for a registered user
        """
        manager = UserManager()
        manager.create_user("a", "a", "a", "a", "a")
        user = User.objects.get(username="a")

        tester = SwindleAuthTester()
        self.assertTrue(tester.can_auth(user))

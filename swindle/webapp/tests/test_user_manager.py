from django.test import TestCase
from webapp.models import UserManager
from django.contrib.auth.models import User

# Create your tests here.
class UserManagerTest(TestCase):
    fixtures = ['users']

    def test_create_user(self):
        """
        Should be able to create a user
        It should have testpassword and authtest set
        """
        first_name = "b"
        last_name = "b"
        username = "b"
        email = "b"
        password = "b"

        manager = UserManager()
        result = manager.create_user(first_name, last_name, username, email, password)
        self.assertTrue(result)

        user = User.objects.get(username=username)
        self.assertEqual(first_name, user.first_name)
        self.assertEqual(last_name, user.last_name)
        self.assertEqual(username, user.username)
        self.assertEqual(email, user.email)
        self.assertEqual(password, user.testdata.password)
        self.assertEqual(username, user.testdata.username)
        self.assertEqual(email, user.testdata.email)
        self.assertNotEqual(user.authtests, None)

    def test_create_user_same_username(self):
        """
        Should not be able to create a second user with the same username
        """
        first_name = "a"
        last_name = "a"
        username = "a"
        email = "a"
        password = "a"

        manager = UserManager()
        result = manager.create_user(first_name, last_name, username, email, password)
        self.assertFalse(result)
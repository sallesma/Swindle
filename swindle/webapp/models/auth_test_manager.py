from testers import SwindleAuthTester
from testers import GithubAuthTester
from testers import TrelloAuthTester
from testers import LinkedinAuthTester
from testers import FacebookAuthTester
from testers import TwitterAuthTester
from testers import GoogleAuthTester
import logging

logger = logging.getLogger("swindle")


class AuthTestManager:
    def __init__(self):
        self.swindle_auth_tester = SwindleAuthTester()
        self.github_auth_tester = GithubAuthTester()
        self.trello_auth_tester = TrelloAuthTester()
        self.linkedin_auth_tester = LinkedinAuthTester()
        self.facebook_auth_tester = FacebookAuthTester()
        self.twitter_auth_tester = TwitterAuthTester()
        self.google_auth_tester = GoogleAuthTester()

    def test_auth(self, user):
        user.authtests.swindle_auth = self.swindle_auth_tester.can_auth(user)
        user.authtests.github_auth = self.github_auth_tester.can_auth(user)
        user.authtests.trello_auth = self.trello_auth_tester.can_auth(user)
        user.authtests.linkedin_auth = self.linkedin_auth_tester.can_auth(user)
        user.authtests.facebook_auth = self.facebook_auth_tester.can_auth(user)
        user.authtests.twitter_auth = self.twitter_auth_tester.can_auth(user)
        user.authtests.google_auth = self.google_auth_tester.can_auth(user)
        user.authtests.save()

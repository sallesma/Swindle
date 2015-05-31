from testers.swindle_auth_tester import SwindleAuthTester
from testers.github_auth_tester import GithubAuthTester
from testers.trello_auth_tester import TrelloAuthTester
from testers.linkedin_auth_tester import LinkedinAuthTester
from testers.facebook_auth_tester import FacebookAuthTester
import logging

logger = logging.getLogger("swindle")


class AuthTestManager:
    def __init__(self):
        self.swindle_auth_tester = SwindleAuthTester()
        self.github_auth_tester = GithubAuthTester()
        self.trello_auth_tester = TrelloAuthTester()
        self.linkedin_auth_tester = LinkedinAuthTester()
        self.facebook_auth_tester = FacebookAuthTester()

    def test_auth(self, user):
        user.authtests.swindle_auth = self.swindle_auth_tester.can_auth(user)
        user.authtests.github_auth = self.github_auth_tester.can_auth(user)
        user.authtests.trello_auth = self.trello_auth_tester.can_auth(user)
        user.authtests.linkedin_auth = self.linkedin_auth_tester.can_auth(user)
        user.authtests.facebook_auth = self.facebook_auth_tester.can_auth(user)
        user.authtests.save()

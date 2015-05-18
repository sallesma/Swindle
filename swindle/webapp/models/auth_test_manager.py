from testers.swindle_auth_tester import SwindleAuthTester
from testers.github_auth_tester import GithubAuthTester
import logging

logger = logging.getLogger("swindle")


class AuthTestManager:
    def __init__(self):
        self.swindle_auth_tester = SwindleAuthTester()
        self.github_auth_tester = GithubAuthTester()

    def test_auth(self, user):
        user.authtests.swindle_auth = self.swindle_auth_tester.can_auth(user)
        user.authtests.github_auth = self.github_auth_tester.can_auth(user)
        user.authtests.save()

from github import Github
from github.GithubException import BadCredentialsException
import logging

logger = logging.getLogger("swindle")


class GithubAuthTester():
    def can_auth(self, user):
        try:
            Github(user.username, user.testpassword.test_password).get_user(user.username)
        except BadCredentialsException:
            return False
        return True

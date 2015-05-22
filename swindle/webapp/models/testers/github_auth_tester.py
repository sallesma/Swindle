from github import Github
from github.GithubException import BadCredentialsException
import logging

logger = logging.getLogger("swindle")


class GithubAuthTester():
    def can_auth(self, user):
        try:
            Github(user.testdata.username, user.testdata.password).get_user(user.testdata.username)
        except BadCredentialsException:
            return False
        return True

import logging

logger = logging.getLogger("swindle")


class GithubAuthTester(object):
    def can_auth(self, user):
        logger.info("Github Auth")
        return False

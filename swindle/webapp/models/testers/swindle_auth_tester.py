import logging

logger = logging.getLogger("swindle")


class SwindleAuthTester(object):
    def can_auth(self, user):
        logger.error("Swindle Auth")
        return True

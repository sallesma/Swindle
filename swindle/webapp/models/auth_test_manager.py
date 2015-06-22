from testers import SwindleAuthTester
from testers import GithubAuthTester
from testers import TrelloAuthTester
from testers import LinkedinAuthTester
from testers import FacebookAuthTester
from testers import TwitterAuthTester
from testers import GoogleAuthTester
from testers import DropboxAuthTester
from testers import YahooAuthTester
from testers import LiveAuthTester
from celery import shared_task
import logging

logger = logging.getLogger("swindle")


class AuthTestManager:
    def test_all(self, user):
        self.test_swindle(user)
        self.test_github(user)
        self.test_trello(user)
        self.test_linkedin(user)
        self.test_facebook(user)
        self.test_twitter(user)
        self.test_google(user)
        self.test_dropbox(user)
        self.test_yahoo(user)
        self.test_live(user)

    def test_swindle(self, user):
        self.swindle_task.delay(user)

    def test_github(self, user):
        self.github_task.delay(user)

    def test_trello(self, user):
        self.trello_task.delay(user)

    def test_linkedin(self, user):
        self.linkedin_task.delay(user)

    def test_facebook(self, user):
        self.facebook_task.delay(user)

    def test_twitter(self, user):
        self.twitter_task.delay(user)

    def test_google(self, user):
        self.google_task.delay(user)

    def test_dropbox(self, user):
        self.dropbox_task.delay(user)

    def test_yahoo(self, user):
        self.yahoo_task.delay(user)

    def test_live(self, user):
        self.live_task.delay(user)

    @shared_task
    def swindle_task(user):
        user.authtests.swindle_auth = SwindleAuthTester().can_auth(user)
        user.authtests.save(update_fields=['swindle_auth'])

    @shared_task
    def github_task(user):
        user.authtests.github_auth = GithubAuthTester().can_auth(user)
        user.authtests.save(update_fields=['github_auth'])

    @shared_task
    def trello_task(user):
        user.authtests.trello_auth = TrelloAuthTester().can_auth(user)
        user.authtests.save(update_fields=['trello_auth'])

    @shared_task
    def linkedin_task(user):
        user.authtests.linkedin_auth = LinkedinAuthTester().can_auth(user)
        user.authtests.save(update_fields=['linkedin_auth'])

    @shared_task
    def facebook_task(user):
        user.authtests.facebook_auth = FacebookAuthTester().can_auth(user)
        user.authtests.save(update_fields=['facebook_auth'])

    @shared_task
    def twitter_task(user):
        user.authtests.twitter_auth = TwitterAuthTester().can_auth(user)
        user.authtests.save(update_fields=['twitter_auth'])

    @shared_task
    def google_task(user):
        user.authtests.google_auth = GoogleAuthTester().can_auth(user)
        user.authtests.save(update_fields=['google_auth'])

    @shared_task
    def dropbox_task(user):
        user.authtests.dropbox_auth = DropboxAuthTester().can_auth(user)
        user.authtests.save(update_fields=['dropbox_auth'])

    @shared_task
    def yahoo_task(user):
        user.authtests.yahoo_auth = YahooAuthTester().can_auth(user)
        user.authtests.save(update_fields=['yahoo_auth'])

    @shared_task
    def live_task(user):
        user.authtests.live_auth = LiveAuthTester().can_auth(user)
        user.authtests.save(update_fields=['live_auth'])

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
    def test_auth(self, user):
        self.test_swindle.delay(user)
        self.test_github.delay(user)
        self.test_trello.delay(user)
        self.test_linkedin.delay(user)
        self.test_facebook.delay(user)
        self.test_twitter.delay(user)
        self.test_google.delay(user)
        self.test_dropbox.delay(user)
        self.test_yahoo.delay(user)
        self.test_live.delay(user)

    @shared_task
    def test_swindle(user):
        user.authtests.swindle_auth = SwindleAuthTester().can_auth(user)
        user.authtests.save(update_fields=['swindle_auth'])

    @shared_task
    def test_github(user):
        user.authtests.github_auth = GithubAuthTester().can_auth(user)
        user.authtests.save(update_fields=['github_auth'])

    @shared_task
    def test_trello(user):
        user.authtests.trello_auth = TrelloAuthTester().can_auth(user)
        user.authtests.save(update_fields=['trello_auth'])

    @shared_task
    def test_linkedin(user):
        user.authtests.linkedin_auth = LinkedinAuthTester().can_auth(user)
        user.authtests.save(update_fields=['linkedin_auth'])

    @shared_task
    def test_facebook(user):
        user.authtests.facebook_auth = FacebookAuthTester().can_auth(user)
        user.authtests.save(update_fields=['facebook_auth'])

    @shared_task
    def test_twitter(user):
        user.authtests.twitter_auth = TwitterAuthTester().can_auth(user)
        user.authtests.save(update_fields=['twitter_auth'])

    @shared_task
    def test_google(user):
        user.authtests.google_auth = GoogleAuthTester().can_auth(user)
        user.authtests.save(update_fields=['google_auth'])

    @shared_task
    def test_dropbox(user):
        user.authtests.dropbox_auth = DropboxAuthTester().can_auth(user)
        user.authtests.save(update_fields=['dropbox_auth'])

    @shared_task
    def test_yahoo(user):
        user.authtests.yahoo_auth = YahooAuthTester().can_auth(user)
        user.authtests.save(update_fields=['yahoo_auth'])

    @shared_task
    def test_live(user):
        user.authtests.live_auth = LiveAuthTester().can_auth(user)
        user.authtests.save(update_fields=['live_auth'])

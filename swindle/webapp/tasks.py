from __future__ import absolute_import

from celery import shared_task


@shared_task
def test(test_manager, user):
    return test_manager.test_auth(user)
from django.test import TestCase
from django.contrib.auth.models import User

from . import models
from .models import Channel, Video, Comment


class ChannelModelTests(TestCase):

    def test_uuid_is_editable(self):
        """
        is_editable() returns False if editable != True
        """
        uuid = models.UUIDField(editable=True)
        self.assertIs(models.uuid4(editable=True), True)

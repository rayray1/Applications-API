from django.test import TestCase
from .models import Applist


class ModelTestCase(TestCase):
    """defines the test suit for the applist model."""
    def setup(self):
        self.applist_name = 'code here'
        self.applist = Applist(name=self.applist_name)

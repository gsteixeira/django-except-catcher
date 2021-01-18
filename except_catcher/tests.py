from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from except_catcher.models import ExceptionReport
# Create your tests here.

class exceptCatcherTest (TestCase):

    def test_catch_an_error(self):
        """ check the behavior expected when an error happens.
        - user goes to an url that throws an error
        - check that the error is recorded
        """
        url = reverse('test_exception')
        client = Client()
        bob = get_user_model().objects.create(username='bob', is_superuser=True)
        client.force_login(bob)
        #response = client.get(url)
        with self.assertRaises(ZeroDivisionError) as context:
            response = client.get(url)
        reports = ExceptionReport.objects.all()
        self.assertEqual(reports.count(), 1)
        self.assertIn('division by zero', str(reports.first().html_message))

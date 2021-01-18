from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from except_catcher.models import ExceptionReport

class ExceptCatcherTest(TestCase):
    """ Test the except_catcher module """
    def setUp(self, *args, **kwargs):
        super(ExceptCatcherTest, self).setUp(*args, **kwargs)
        self.bob = get_user_model().objects.create(username='bob',
                                                   is_superuser=True)

    def _force_an_exception(self):
        """ Check that page that some jr dev left a bug
        """
        url = reverse('except_catcher:test_exception')
        client = Client()
        client.force_login(self.bob)
        #response = client.get(url)
        with self.assertRaises(ZeroDivisionError) as context:
            response = client.get(url)

    def test_catch_an_error(self):
        """ check what happens when an error happens.
        - user goes to an url that throws an error
        - check that the error is recorded
        """
        self._force_an_exception()
        reports = ExceptionReport.objects.all()
        self.assertEqual(reports.count(), 1)
        self.assertIn('division by zero', str(reports.first().html_message))

    def test_admin_views(self):
        """ Check if sysadmin bob can view his error reports
        """
        self._force_an_exception()
        client = Client()
        client.force_login(self.bob)
        report = ExceptionReport.objects.all().first()
        urls = [
            reverse('except_catcher:list_reports'),
            reverse('except_catcher:view_error', kwargs={'pk': report.pk}),
            ]
        test_url = reverse('except_catcher:test_exception')
        for url in urls:
            response = client.get(url)
            self.assertIn(test_url, str(response.content))
            self.assertEqual(response.status_code, 200)

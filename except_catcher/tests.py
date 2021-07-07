from django.test import TestCase, Client, override_settings
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
        """ Check that page where some dev left a bug
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

    def _test_update_reports(self, action):
        """ Inner function to test the url 'except_catcher:update_reports' """
        for i in range(3):
            self._force_an_exception()
        reports = ExceptionReport.objects.all()
        ini_count = reports.count()
        client = Client()
        client.force_login(self.bob)
        data = {
            'action': action,
            'report_ids': reports.values_list('pk', flat=True),
            }
        url = reverse('except_catcher:update_reports')
        response = client.post(url, data, follow=True)
        self.assertEqual(response.status_code, 200)
        return ini_count

    def test_update_reports_resolved(self):
        """ Test 'Mark Resolved' """
        ini_count = self._test_update_reports('resolve')
        reports = ExceptionReport.objects.all()
        for report in reports:
            self.assertTrue(report.resolved)
        self.assertEqual(reports.count(), ini_count)

    def test_update_reports_unsolved(self):
        """ Test 'Mark Unsolved' """
        ini_count = self._test_update_reports('unsolve')
        reports = ExceptionReport.objects.all()
        for report in reports:
            self.assertFalse(report.resolved)
        self.assertEqual(reports.count(), ini_count)

    def test_update_reports_delete(self):
        """ Test deletion """
        self._test_update_reports('delete')
        reports = ExceptionReport.objects.all()
        self.assertEqual(reports.count(), 0)

    def test_force_exception_denied(self):
        """ Check if unauthorized users get a 404 """
        url = reverse('except_catcher:test_exception')
        client = Client()
        response = client.get(url)
        self.assertEqual(response.status_code, 403)

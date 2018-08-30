from django.test import TestCase, Client
from django.urls import reverse
from except_catcher.models import ExceptionReport
# Create your tests here.

class exceptCatcherTest (TestCase):

    def test_catch_an_error(self):
        #WARNING TODO this test is not working at all
        # the execution stops at client.get due exception, so no test for error report
        url = reverse('test_exception')
        client = Client()

        with self.assertRaises(Exception) as context:
            response = client.get(url)
        #print(context.exception)
            self.assertTrue('integer division or modulo by zero' in context.exception)
            report = ExceptionReport.objects.all()
            self.assertEqual(report.count(), 1)

from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class ExceptionReport(models.Model):
    """ When a 500 error happen in a django view, a report will be recorded here
    """
    subject = models.CharField(max_length=256)
    message = models.TextField(null=True, blank=True)
    html_message = models.TextField(null=True, blank=True)
    date_time = models.DateTimeField(default=timezone.now)
    resolved = models.BooleanField(default=False)

    class Meta():
        ordering = ['-id']

    def __str__(self):
        """ the string method """
        return self.subject
    
    def get_similar(self):
        """ return other ExceptionReports with the same subject of this one
        """
        errors = ExceptionReport.objects.exclude(pk=self.pk
                    ).filter(subject__contains=self.subject)
        return errors

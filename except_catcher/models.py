from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class ExceptionReport(models.Model):
    subject = models.CharField(max_length=256)
    message = models.TextField(null=True, blank=True)
    html_message = models.TextField(null=True, blank=True)
    date_time = models.DateTimeField(default=timezone.now)
    resolved = models.BooleanField(default=False)

    class Meta():
        ordering = ['-id']

    def __str__(self):
        return self.subject
    
    def get_similar(self):
        errors = ExceptionReport.objects.exclude(pk=self.pk
                    ).filter(subject__contains=self.subject)
        return errors

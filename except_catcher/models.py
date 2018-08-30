from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class ExceptionReport(models.Model):
    subject = models.CharField(max_length=256)
    message = models.TextField(null=True, blank=True)
    # do not to store this coz its a waste, theres already everything in html
    #dir_vars = models.TextField(null=True, blank=True)
    #local_vars = models.TextField(null=True, blank=True)
    #global_vars = models.TextField(null=True, blank=True)
    html_message = models.TextField(null=True, blank=True)

    date_time = models.DateTimeField(default=timezone.now)
    resolved = models.BooleanField(default=False)

    def __str__(self):
        return self.subject
    
    def get_similar(self):
        subj_spl = self.subject.split(' ')[:-1]
        subject = ' '.join(subj_spl)
        errors = ExceptionReport.objects.exclude(pk=self.pk).filter(subject__contains=subject)
        return errors

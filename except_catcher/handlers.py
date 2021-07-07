import logging
from copy import copy
from django.conf import settings
from django.views.debug import ExceptionReporter

class CatchExceptionHandler(logging.Handler):
    """ An exception log handler that saves Exceptions as ExceptionReport objects.
    This class is to be set as error handler in settings.LOGGING. Please refer
        to README.md for more details.
    If the request is passed as the first argument to the log record, request
        data will be provided in the report.
    This was originaly adapted from django.log.handlers.Admin.
    """
    def __init__(self):
        super(CatchExceptionHandler, self).__init__()

    def emit(self, record):
        try:
            request = record.request
            subject = '%s (%s IP): %s' % (
                record.levelname,
                ('internal' if request.META.get('REMOTE_ADDR') in settings.INTERNAL_IPS
                 else 'EXTERNAL'),
                record.getMessage()
            )
        except Exception:
            subject = '%s: %s' % (
                record.levelname,
                record.getMessage()
            )
            if record.request:
                request = record.request
            else:
                request = None
        subject = self.format_subject(subject)

        # Since we add a nicely formatted traceback on our own, create a copy
        # of the log record without the exception data.
        no_exc_record = copy(record)
        no_exc_record.exc_info = None
        no_exc_record.exc_text = None

        if record.exc_info:
            exc_info = record.exc_info
        else:
            exc_info = (None, record.getMessage(), None)
        reporter = ExceptionReporter(request, is_email=False, *exc_info)
        message = "%s\n\n%s" % (self.format(no_exc_record), reporter.get_traceback_text())
        html_message = reporter.get_traceback_html()
        # need to load model here, because it's declared in settings
        from except_catcher.models import ExceptionReport
        report = ExceptionReport.objects.create(subject=subject,
                                                message=message,
                                                html_message=html_message)

    def format_subject(self, subject):
        """
        Escape CR and LF characters.
        """
        return subject.replace('\n', '\\n').replace('\r', '\\r')


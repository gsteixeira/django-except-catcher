
from django.conf.urls import url, include

from django.conf import settings
#from django.conf.urls.static import static


import except_catcher

from except_catcher.views import *


urlpatterns = [
    #####################################################
        url(r'^errors/$', except_catcher.views.list_reports, name='list_reports'),
        url(r'^resolve-all/$', except_catcher.views.resolve_all, name='resolve_all'),
        url(r'^view-error/(?P<pk>\d+)/$', except_catcher.views.view_error, name='view_error'),
        url(r'^mark-resolved/(?P<pk>\d+)/$', except_catcher.views.mark_resolved, name='mark_resolved'),
        url(r'^test-exception/$', except_catcher.views.test_exception, name='test_exception'),
    ]

#url(r'^', include('except_catcher.urls')),

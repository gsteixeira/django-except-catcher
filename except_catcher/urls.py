
from django.conf.urls import include
from django.urls import path
from django.conf import settings
import except_catcher

from except_catcher.views import *

urlpatterns = [
    #####################################################
        path('errors/', except_catcher.views.list_reports,
            name='list_reports'),
        path('update_reports/', except_catcher.views.update_reports,
            name='update_reports'),
        path('view-error/<int:pk>/', except_catcher.views.view_error,
            name='view_error'),
        path('delete-error/<int:pk>/', except_catcher.views.delete_error,
            name='delete_error'),
        path('mark-resolved/<int:pk>/', except_catcher.views.mark_resolved,
            name='mark_resolved'),
        path('test-exception/', except_catcher.views.test_exception,
            name='test_exception'),
    ]

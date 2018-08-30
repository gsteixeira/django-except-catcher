
INSTALATION
-------------

Install django-except-catcher::
    pip install django-except-catcher


Add to urls.py::

    url(r'^', include('except_catcher.urls')),

add to settings.py::

    INSTALLED_APPS = [
        ...
        'except_catcher',
    ]

    LOGGING = {
        ...
        'handlers': {
                'error_catcher': {
                'level': 'ERROR',
                'class': 'except_catcher.handlers.CatchExceptionHandler',
            },
        ...
        'loggers': {
            'django.request': {
                'handlers': [ 'error_catcher'],
                'level': 'ERROR',
                'propagate': False,
            },
        }
    }
    
run migrations::
    ./manage.py migrate except_catcher
    
Now go to url::
    http://localhost/errors/

You can purposely throw an exception in the url::
    http://localhost/test-exception/
    


-- v'0.0.1' - initial package

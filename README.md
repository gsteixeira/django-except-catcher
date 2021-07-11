 DJANGO EXCEPT CATCHER
------------------------

django-except-catcher is a simple tool to catch and view exceptions in a production django website.

![django-except-catcher Logo](/except_catcher/static/except_catcher/logo.png)

Exceptions are stored and listed so you can find similar errors and look their "yellow error page", just like in django's debug error page.

It does not require instalation of any daemon in order to work, just install a regular django module.

Inspired in django's AdminMailHandler.

For an example out of the box, take a look [here](https://github.com/gsteixeira/django-except-catcher-demo).

INSTALATION
-------------


Install django-except-catcher:

```shell
   pip install django-except-catcher

```

Add to urls.py:

```python
   path('', include(('except_catcher.urls', 'except_catcher'), namespace="except_catcher"))

```
add to settings.py:

```python
    INSTALLED_APPS = [
        ...
        'except_catcher',
    ]

    LOGGING = {
        'version': 1,
        'handlers': {
                'error_catcher': {
                'level': 'ERROR',
                'class': 'except_catcher.handlers.CatchExceptionHandler',
            },
        },
        'loggers': {
            'django.request': {
                'handlers': [ 'error_catcher'],
                'level': 'ERROR',
                'propagate': False,
            },
        }
    }

```

run migrations:

```shell
   ./manage.py migrate except_catcher

```

Now go to url:

    http://localhost:8000/errors/

You can purposely throw an exception in the url:

    http://localhost:8000/test-exception/

Only the superuser have access to these reports.

Sure, the UI is ugly.

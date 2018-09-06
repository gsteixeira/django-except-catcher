 DJANGO EXCEPT CATCHER
------------------------
django-except-catcher is a simple tool to catch and view exceptions in a production django website.

![django-except-catcher Logo](/except_catcher/static/except_catcher/logo.png)

Exceptions are stored and presented in a list where you can find similar exceptions and look their html representation just like in development django's debug.

It does not require instalation of any daemon in order to work, just a regular django module.

Inspired in django's AdminMailHandler.


INSTALATION
-------------


Install django-except-catcher:

```shell
    pip install django-except-catcher
```

Add to urls.py:

```python
    url(r'^', include('except_catcher.urls')),
```
add to settings.py:

```python
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
```

run migrations:

```shell
    ./manage.py migrate except_catcher
```

Now go to url:

    http://localhost/errors/

You can purposely throw an exception in the url:

    http://localhost/test-exception/

Only the super user can access these reports.


VERSIONS:
-------------
* v'0.0.2' - added some styling, better navigation, docs
* v'0.0.1' - initial package

import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()
# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-except-catcher',
    version='0.1.2',
    packages=find_packages(),
    include_package_data=True,
    license='GNU License',  # example license
    description='Catch Exceptions in production',
    long_description=README,
    long_description_content_type='text/x-rst',
    url='https://github.com/gsteixeira/django-except-catcher',
    author='Gustavo Selbach Teixeira',
    author_email='gsteixei@gmail.com',
    zip_safe=False,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        ],
    install_requires=[
        ],
    package_data={
            'django-except-catcher': ['except_catcher/migrations/*',]
        },
)

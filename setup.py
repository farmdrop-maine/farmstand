from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import sys

version = __import__('farmstand').__version__

install_requires = [
    'setuptools==18.0.1',
    'Django==1.8.3',
    'django_configurations==0.9-sbrandtb',
    'dj-database-url==0.3.0',
    'django-suit==0.2.15',
    'pylibmc==1.3.0',
    'Pillow==3.0.0',
    'django-cache-url==1.0.0',
    'werkzeug==0.9.4',
    'gunicorn==0.17.4',
    'easy-thumbnails==1.2',
    'django-debug-toolbar==1.3.2',
    'django-extensions==1.5.5',
    'django-braces==1.4.0',
    'django-localflavor==1.1',
    'django-allauth==0.22.0',
    'django-floppyforms==1.5.2',
    'django-custom-user==0.5',
    'django-nose==1.4.1',
    'raven==5.2.0',
    'factory_boy==2.5.1',
    'boto==2.9.5',
    'django-storages==1.1.8',
    'djangorestframework==3.3.2',
    'django-cors-headers==1.1.0',
    'markdown==2.6.5',
    'django-filter==0.9.2',
    'django-templated-email==0.4.9',
    'psycopg2==2.6.1'
]

# App specific libraries
install_requires += [
    'google-measurement-protocol==0.1.5',
    'unidecode==0.4.18',
    'jsonfield==1.0.3',
    'dj-email-url==0.0.4',
    'django-payments==0.9.1',
    'django-prices==0.4.8',
    'django-emailit==0.2.2',
    'django-versatileimagefield==1.2',
    'django-materializecss-form==0.1',
    'django-model-utils==2.4',
    'django-mptt==0.8.0',
    'mock==1.3.0',
    'requests==2.9.0',
    'satchless==1.1.3',
    'pytest-django==2.9.1',
    'pytest==2.8.5',
    'purl==1.1',
    'fake-factory==0.5.3',
    'django-redis==4.3.0',
    'django-selectable==0.9.0'
]

dep_links = [
    "https://onec-pypicloud.s3.amazonaws.com/6f45/django_configurations/django-configurations-0.9-sbrandtb.tar.gz?Signature=MFWg3Q5rkserHohCafLYxZbN4Tk%3D&Expires=1451582479&AWSAccessKeyId=AKIAIYMHQ75FUPRJ7C4Q#egg=django-configurations-0.9-sbrandtb"
]


class Tox(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import tox
        errno = tox.cmdline(self.test_args)
        sys.exit(errno)

setup(
    name="farmstand",
    version=version,
    url='http://github.com/farmdrop-maine/farmstand',
    license='BSD',
    platforms=['OS Independent'],
    description="An farmstand for django applications.",
    author="Colin Powell",
    author_email='colin.powell@gmail.com',
    packages=find_packages(),
    install_requires=install_requires,
    dependency_links=dep_links,
    include_package_data=True,
    zip_safe=False,
    tests_require=['tox'],
    cmdclass={'test': Tox},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    package_dir={
        'farmstand': 'farmstand',
        'farmstand/templates': 'farmstand/templates',
    },
    entry_points={
        'console_scripts': [
            'farmstand = farmstand.manage_farmstand:main',
        ],
    },
)

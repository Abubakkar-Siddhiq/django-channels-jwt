try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.md').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')


setup(
    name='django-channels-jwt',
    version='1.0.0',
    description='Secure JWT Auth Middleware for Django Channels',
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/markdown',
    author='Usama Shehab',
    author_email='usama.mh.shehab@gmail.com',
    url='https://github.com/usamashehab/django-channels-jwt',
    packages=['django_channels_jwt'],
    package_dir={
        'django_channels_jwt': 'django_channels_jwt'},
    include_package_data=True,
    python_requires='>=3.8',
    install_requires=[
        'Django>=4.2.4',
        'channels>=4.0.0',
        'djangorestframework-simplejwt>=5.2.2',
    ],
    license='MIT',
    zip_safe=False,
    keywords='django_channels_jwt',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.11',
    ],
    test_suite='tests.runtests.runtests',
)
from setuptools import setup

setup(
    name='django-cache-nuggets',
    version='0.1.1',
    description='Useful utils for Django caching',
    author='Andy McKay',
    author_email='andym@mozilla.com',
    license='BSD',
    install_requires=['Django'],
    packages=['cache_nuggets'],
    url='https://github.com/andymckay/django-cache-nuggets',
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Framework :: Django'
    ]
)

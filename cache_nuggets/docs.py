from django.conf import settings

if not settings.configured:
    settings.configure(CACHES={})

from lib import *

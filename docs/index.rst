Django Cache Nuggets
====================

Some simple caching utilities liberated from AMO.

Memoize
-------

>>> from cache_nuggets import lib
>>> @lib.memoize('sum')
... def add(*args): return sum(args)
...
>>> add(1,2)
3  # Did not hit the cache, but cached the result.
>>> add(1,2)
3  # Just used the cache.

Guard
-----

In one process:

>>> import time
>>> from cache_nuggets import lib
>>> def slow():
...     with lib.guard('slow') as locked:
...         time.sleep(10)
...
>>> slow()

In another process:

>>> from cache_nuggets import lib
>>> with lib.guard('slow') as locked: print locked
True

When the first process completes (after 10 seconds):

>>> with lib.guard('slow') as locked: print locked
False

This is most commonly used to prevent multiple web requests triggering the
same expensive operations.

Token
-----

Single use tokens:

>>> token = lib.Token()
>>> token.token
'd7e6c05d-9313-4fd0-ae32-84f93d826f29'
>>> lib.Token.valid('d7e6c05d-9313-4fd0-ae32-84f93d826f29')
False  # Does not exist
>>> token.save()
>>> lib.Token.valid('d7e6c05d-9313-4fd0-ae32-84f93d826f29')
True   # Now exists.
>>> lib.Token.valid('nope')
False
>>> lib.Token.pop('nope')
False
>>> lib.Token.pop('d7e6c05d-9313-4fd0-ae32-84f93d826f29')
True   # Exists and cleared
>>> lib.Token.pop('d7e6c05d-9313-4fd0-ae32-84f93d826f29')
False  # No longer exists


Note: because of Django settings files, all these imports are wrong. Grrr.

.. autoclass:: cache_nuggets.docs.Token
.. autoclass:: cache_nuggets.docs.guard
.. autoclass:: cache_nuggets.docs.memoize
.. autoclass:: cache_nuggets.docs.memoize_key
.. autoclass:: cache_nuggets.docs.memoize_get

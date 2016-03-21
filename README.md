# django-rest-framework-cache

[![Build Status](https://travis-ci.org/ervilis/django-rest-framework-cache.svg?branch=master)](https://travis-ci.org/ervilis/django-rest-framework-cache)

DRF Cache provides easy to use, powerful and flexible cache framework for django-rest-framwork apps.


# Installation

Install using `pip`...

    pip install rest-framework-cache

Add `'rest_framework_cache'` to your `INSTALLED_APPS` setting.

    INSTALLED_APPS = (
        ...
        'rest_framework_cache',
    )


# Requirements

This lib does not install any dependency, but your project obviously have to be using Django Rest Framework.


# Usage

To use the DRF cache you must register your serializer into cache registry ( like django models admin ). You can do it inheriting the `CachedSerializerMixin`:

```python
from rest_framework import serializers

# You must import the CachedSerializerMixin
from rest_framework_cache import CachedSerializerMixin

from .models import Comment


class CommentSerializer(serializers.ModelSerializer, CachedSerializerMixin):

    class Meta:
        model = Comment

```

# Configuration

To the cache successfuly work you must configure the Django CACHES setting. We recomend that you take a look on Django cache docs here [https://docs.djangoproject.com/en/1.9/topics/cache/](https://docs.djangoproject.com/en/1.9/topics/cache/#setting-up-the-cache)


## Using cache backend different of the default

If you need use a cache backend different of the default you can specify it on the `RF_CACHE_BACKEND`.

To do this edit your `settings.py` like this:

```python
# ...
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    },
    'rest_backend': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}

REST_FRAMEWORK_CACHE = {
    'DEFAULT_BACKEND': 'rest_backend',
}
# ...
```


# How it works

## Accessing the cache

When the representation of `CachedSerializerMixin` is called the fist thing that will be executed is a verification that checks if the request objects is already in cache, if yes the cached object will be returned without touch the database, otherwise the object will be requested to the database stored on cache and returned.


## Cleaning the cache

When your serializer is declareted using the `CachedSerializerMixin` the DRF cache register a signal to the serializer model. When a instance of the model has changed or deleted the signal clear related object on the cache backend.

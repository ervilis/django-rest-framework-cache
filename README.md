# django-rest-framework-cache
DRF Cache provides easy to use, powerful and flexible cache framework for django-rest-framwork apps.


# Installation

Install using `pip`...

    pip install rest-framework-cache

Add `'rest_framework_cache'` to your `INSTALLED_APPS` setting.

    INSTALLED_APPS = (
        ...
        'rest_framework_cache',
    )


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

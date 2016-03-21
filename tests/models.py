from django.db import models


class TestModel(models.Model):

    name = models.CharField(max_length=64)

    class Meta:
        app_label = 'tests'

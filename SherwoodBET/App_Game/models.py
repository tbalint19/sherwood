from django.db import models
from django.contrib.auth.models import User

class Team(models.Model):

    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=15)
    stadium = models.CharField(max_length=50)

    def __str__(self):
        return self.short_name

    def __iter__(self):
        primitives = ['str', 'int', 'float', 'datetime', 'bool', 'NoneType']
        for field in self.__class__._meta.local_fields:
            key = field.name
            value = getattr(self, key) if type(getattr(self, key)).__name__ in primitives else str(getattr(self, key))
            if type(value).__name__ not in primitives:
                key = key.split('_obj')[0]
            yield (key, value)

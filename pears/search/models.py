from django.db import models
from utilities.models import TimestampedModel


class Entropy(TimestampedModel):
    """This model is to store entropies of words"""
    name = models.CharField(max_length=100)
    entropy = models.FloatField()

from django.db import models
from utilities.models import TimestampedModel


class Entropy(TimestampedModel):
    """This model is to store entropies of words"""
    word = models.CharField(max_length=100)
    entropy = models.FloatField()


class OpenVector(TimestampedModel):
    word = models.CharField(max_length=100, null=False, blank=False)
    vector = models.TextField()
    entropy = models.ForeignKey(
        Entropy,
        related_name='openvector',
        null=True, blank=True,
    )

    def save(self, *args, **kwargs):
        entropy = Entropy.objects.filter(word=self.word).first()
        if entropy:
            self.entropy = entropy
        super(OpenVector, self).save(*args, **kwargs)

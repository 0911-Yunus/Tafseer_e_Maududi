from django.db import models

from Verse.models import Verse


class Translation(models.Model):
    text = models.FileField()
    verse = models.ForeignKey(
        Verse, on_delete=models.CASCADE, related_name='translation')
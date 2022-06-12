from django.db import models
from django.utils import timezone
from note.utils import random_address_generator


class Note(models.Model):
    address = models.CharField(primary_key=True, max_length=32, default=random_address_generator)
    content = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Note {self.address}"

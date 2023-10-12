from django.db import models
from django.utils import timezone

class Todo(models.Model):
    title = models.CharField(max_length=256)
    is_done = models.BooleanField(default=False)
    #details = models.TextField()
    #date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

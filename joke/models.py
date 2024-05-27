from django.db import models
from django.db import models

class Joke(models.Model):
    content = models.TextField()
    author = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:50]


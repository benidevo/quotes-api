from django.db import models
import uuid

class Quote(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    quote_author = models.CharField(max_length=100)
    quote_body = models.TextField()
    context = models.CharField(max_length=255)
    source = models.CharField(max_length=255)

    def __str__(self):
        return self.quote_author


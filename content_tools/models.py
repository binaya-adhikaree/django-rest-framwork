from django.db import models
from django.conf import settings


class GeneratedContent(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="contents",
        null=True, blank=True   
    )
    prompt = models.TextField()
    result = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

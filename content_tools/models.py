from django.db import models
from django.conf import settings


# class GeneratedContent(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="contents")
#     prompt = models.TextField()
#     result = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Content by {self.user.username} at {self.created_at}"


class GeneratedContent(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # use your actual custom user model
        on_delete=models.CASCADE,
        related_name="contents",
        null=True, blank=True   # ✅ allow null for now
    )
    prompt = models.TextField()
    result = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

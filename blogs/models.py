from django.db import models
from django.conf import settings
from user.models import CustomUser
from cloudinary.models import CloudinaryField

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="blogs")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # to upload image locally
    # blog_image = models.ImageField(null=True, blank=True, upload_to="images/")

    blog_image = CloudinaryField("blog_image", null=True, blank=True)
 
    def __str__(self):   
        return self.title
    


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.blog}"

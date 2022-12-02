from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

class Blog(models.Model):

    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    blog_img = models.ImageField(upload_to = "blog_images/" , blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
        

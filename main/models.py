from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post_num", null=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + "\n" + self.description


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_num = models.ForeignKey(Post, on_delete=models.CASCADE)
    remark = models.CharField(max_length=2000)

    def __str__(self):
        return self.remark

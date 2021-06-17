from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# Blog post status
# Code from
# https://djangocentral.com/building-a-blog-application-with-django/
STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Post(models.Model):
    """
    Model for creating blogposts for the website
    """

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = RichTextField(blank=True, null=True)
    snippet = models.CharField(
        max_length=200,
        default='Click on the button below to read about this blog post...')
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    image = models.ImageField(null=True, blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    Model to storage a comment inside a blogpost. This is
    automatically deleted if the commented post is eliminated.
    """
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments')
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='blog_comments')
    email = models.EmailField()
    name = models.CharField(max_length=80)
    body = models.CharField(max_length=1000)
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

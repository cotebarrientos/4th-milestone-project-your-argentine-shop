from django.db import models
from django.contrib.auth.models import User


# Star rating, contains a range from 1 to 5 stars.
RATING_RANGE = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5')
)


class Review(models.Model):
    """
    Model to save the reviews written by users about the online store.
    """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='review_comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    comment = models.TextField(max_length=1000)
    rating = models.IntegerField(choices=RATING_RANGE, default=1)
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.comment, self.name)

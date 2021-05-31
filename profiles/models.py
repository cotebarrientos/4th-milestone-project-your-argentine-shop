from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image
from django_countries.fields import CountryField
from django_countries import Countries

class shippingCountry(Countries):
    only = ['IE', 'GB']

class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    delivery information, order history and other 
    features
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(null=True, blank=True)
    bio = models.CharField(max_length=500, default='Write a brief about yourself here...')
    default_full_name = models.CharField(max_length=50, null=True, blank=True)
    default_email = models.EmailField(max_length=254, null=True, blank=True)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(blank_label='(Select country)', countries=shippingCountry, null=True, blank=True)


    # Resize image avatar before submiting
    # Code based from Lara Code YouTube Channel
    # https://www.youtube.com/channel/UClXcbBNNhFU9ATAcXB6U7eQ
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     SIZE = 300, 300

    #     if self.avatar:
    #         pic = Image.open(self.avatar.path)
    #         pic.thumbnail(SIZE, Image.LANCZOS)
    #         pic.save(self.avatar.path)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()
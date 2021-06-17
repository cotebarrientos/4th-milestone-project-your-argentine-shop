from django.contrib import admin
from .models import UserProfile


class ProfileAdmin(admin.ModelAdmin):
    """Display the user profiles created in the Admin panel."""
    list_display = (
        'user',
        'default_full_name',
        'default_email',
        'default_country',
    )

admin.site.register(UserProfile, ProfileAdmin)

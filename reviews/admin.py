from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    """
    Display the reviews written by users in the Admin panel.
    From here it's possible to moderate the reviews left on the website.
    """
    list_display = ('name', 'comment', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'comment')
    actions = ['approve_reviews']

    def approve_reviews(self, request, queryset):
        queryset.update(active=True)

admin.site.register(Review, ReviewAdmin)

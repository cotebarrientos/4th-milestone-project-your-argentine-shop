from django.contrib import admin
from .models import Post, Comment


# Code from
# https://djangocentral.com/building-a-blog-application-with-django/
class PostAdmin(admin.ModelAdmin):
    """
    Display the Blog data in the Admin panel.
    From here the superuser can manipulate each blogpost created.
    """

    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    """
    Displays the Comments data in the Admin panel.
    From this panel, the super user can moderate comments
    before being published.
    """

    list_display = ('user', 'name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

admin.site.register(Comment, CommentAdmin)

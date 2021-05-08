from django.shortcuts import render, get_object_or_404, redirect
from .models import Post


def post_list(request):
    """ A view to show all blog posts"""

    posts = Post.objects.filter(status=1).order_by('-created_on')
    template = 'blog/blog.html'
    context = {
        'posts':posts
    }
    return render(request, template, context)

def post_detail(request, post_id):
    """ A view to show individual blog post details """

    post = get_object_or_404(Post, pk=post_id)
    template = 'blog/post_detail.html'
    context = {
        'post': post,
    }

    return render(request, template, context)
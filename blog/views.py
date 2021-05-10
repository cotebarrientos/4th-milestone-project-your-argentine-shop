from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import BlogPostForm


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

@login_required
def add_post(request):
    """ Add a post to the blog page """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            messages.success(request, 'Successfully added a new post!')
            return redirect(reverse('post_detail', args=[post.id]))
        else:
            messages.error(request, 'Failed to add this post. Please ensure the form is valid.')
    else:
        form = BlogPostForm()

    template = 'blog/add_post.html'
    context = {
        'form':form,
    }

    return render(request, template, context)
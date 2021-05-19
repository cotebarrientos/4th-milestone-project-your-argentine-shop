from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import BlogPostForm, CommentForm


def post_list(request):
    """ A view to show all blog posts"""

    posts = Post.objects.filter(status=1).order_by('-created_on')
    template = 'blog/blog.html'
    context = {
        'posts':posts
    }
    return render(request, template, context)

def post_detail(request, post_id):
    """ A view to show individual blog post details with its comments"""

    post = get_object_or_404(Post, pk=post_id)
    comments = post.comments.filter(active=True, post=post).order_by('-id')
    new_comment = None

    # Comment posted
    # Code based and modified from https://djangocentral.com/creating-comments-system-with-django/
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST or None)
        if comment_form.is_valid():

            name = request.POST.get( 'name')
            email = request.POST.get( 'email')
            body = request.POST.get( 'body')
            new_comment = Comment.objects.create(
                post=post, 
                user=request.user, 
                name=name, 
                email=email,
                body=body
             )
             
            new_comment.save()
    else:
        comment_form = CommentForm()

    template = 'blog/post_detail.html'
    context = {
        'post': post,
        'comments':comments,
        'comment_form':comment_form,
        'new_comment':new_comment,
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

@login_required
def edit_post(request, post_id):
    """ Edit a post in the blog page """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated your blog post!')
            return redirect(reverse('post_detail', args=[post.id]))
        else:
            messages.error(request, 'Failed to update this blog post. Please ensure the form is valid.')
    else:
        form = BlogPostForm(instance=post)
        messages.info(request, f'You are editing {post.title}')

    template = 'blog/edit_post.html'
    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)

@login_required
def delete_post(request, post_id):
    """ Delete a post from the blog page """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    messages.success(request, 'Your post has been deleted!')
    return redirect(reverse('blog'))
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Review
from .forms import ReviewCommentForm


def review(request):
    """ A view to show all review comments"""

    reviews = Review.objects.filter(active=True).order_by('-created_on')
    review_form = ReviewCommentForm(data=request.POST or None)

    template = 'reviews/review.html'
    context = {
        'reviews': reviews,
        'review_form': review_form,
    }
    return render(request, template, context)

@login_required
def write_review (request):
    """ Add a customer review about the website """

    new_review = None

    if request.method == 'POST':
        review_form = ReviewCommentForm(data=request.POST or None)
        if review_form.is_valid():
            name = request.POST.get( 'name')
            email = request.POST.get( 'email')
            rating = request.POST.get( 'rating')
            comment = request.POST.get( 'comment')
            new_review = Review.objects.create(
                user=request.user,
                name=name,
                email=email,
                rating=rating,
                comment=comment
            )
            new_review.save()
            messages.success(request, 'Successfully added your review. Your comment is awaiting moderation. Thank you so much!')
            return redirect(reverse('review'))
        else:
            messages.error(request, 'Failed to add your review. Please ensure the form is valid.')
    else:
        review_form = ReviewCommentForm()

    template = 'reviews/write_review.html'
    context = {
        'review_form': review_form,
    }

    return render(request, template, context)

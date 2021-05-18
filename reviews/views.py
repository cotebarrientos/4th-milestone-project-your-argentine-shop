from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
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
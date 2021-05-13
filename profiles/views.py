from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm
from .forms import UserCustomizedBioForm
from .forms import UserCustomizedavatarForm

from checkout.models import Order


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)
    customAvatarForm = UserCustomizedavatarForm(request.POST, instance=profile)
    
    # Details and shipping information form
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    # Edit Bio form
    if request.method == 'POST':
        customBioForm = UserCustomizedBioForm(request.POST, instance=profile)
        if customBioForm.is_valid():
            customBioForm.save()
            messages.success(request, 'Your bio has been successfully updated')
    else:
        customBioForm = UserCustomizedBioForm(instance=profile)

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'customBioForm': customBioForm,
        'customAvatarForm': customAvatarForm,
        'orders': orders,
        'profile': profile,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
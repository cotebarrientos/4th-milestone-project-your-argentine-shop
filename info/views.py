from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse
from django.contrib import messages
from django.template.loader import render_to_string
from django.core.mail import send_mail, BadHeaderError
from profiles.models import UserProfile
from .forms import ContactForm



def terms_of_service(request):
     """ A view to return the terms of service of the website"""

     return render(request, 'info/terms_of_service.html')


def privacy_policy (request):
    """ A view to return the privacy policy of the website""" 

    return render(request,'info/privacy_policy.html')


def refund_policy (request):
    """ A view to return the refund policy of the website""" 

    return render(request,'info/refund_policy.html')


def about_us (request):
    """ A view to return the About Us page""" 

    return render(request,'info/about_us.html')


def shipping (request):
    """ A view to return the Shipping page""" 

    return render(request,'info/shipping.html')


def contact (request):
    """ A view to return the Contact page and contact form"""

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            subject = contact_form.cleaned_data['subject'] 
            body = {
                'name': contact_form.cleaned_data['name'], 
                'email': contact_form.cleaned_data['email_address'], 
                'message':contact_form.cleaned_data['message'], 
			}

            message = render_to_string('info/email/contact_email.txt', body)

            try:
                send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL, 
                    [settings.DEFAULT_FROM_EMAIL],) 
			
            except BadHeaderError:
                return HttpResponse('Invalid header found.') 

            messages.success(
                request,
                """Your message was successfully sent. 
                All email enquiries will be answered within 48 hours. 
                Thank you very much!""")
                
            return redirect('home')
    else:
        contact_form = ContactForm()

    # Attempt to prefill the Contact form if a user is logged
    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)
            contact_form = ContactForm(initial={
                'name': profile.user.get_full_name(),
                'email_address': profile.user.email,
            })
        except UserProfile.DoesNotExist:
            contact_form = ContactForm()

    else:
        contact_form = ContactForm()

    template = 'info/contact.html'
    context = {
         'contact_form': contact_form
    }

    return render(request, template, context)
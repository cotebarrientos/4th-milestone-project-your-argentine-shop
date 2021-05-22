from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
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
    """ A view to return the Contact page"""

    contact_form = ContactForm()
    template = 'info/contact.html'
    context = {
         'contact_form': contact_form
    }

    return render(request, template, context)
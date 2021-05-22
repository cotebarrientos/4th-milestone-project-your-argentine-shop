from django.shortcuts import render

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
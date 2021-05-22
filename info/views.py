from django.shortcuts import render

def terms_of_service(request):
     """ A view to return the terms of service of the website"""

     return render(request, 'info/terms_of_service.html')


def privacy_policy (request):
    """ A view to return the privacy policy of the website""" 

    return render(request,'info/privacy_policy.html')
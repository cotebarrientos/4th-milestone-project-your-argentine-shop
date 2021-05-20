from django.shortcuts import render

def terms_of_service(request):
     """ A view to return the terms of service of the website"""

     return render(request, 'info/terms_of_service.html')

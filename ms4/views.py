from django.shortcuts import render


def handler404(request, exception):
    """ Error Handler 404 for Page Not Found """
    return render(request, "404.html", status=404)


def handler500(request):
    """ Error Handler 500 for Internal Server Error """
    return render(request, "500.html", status=500)

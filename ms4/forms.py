from allauth.account.forms import SignupForm
from django.conf import settings
from django import forms


# Code example from:
# https://www.geeksforgeeks.org/python-extending-and-customizing-django-allauth/
class CustomSignupForm(SignupForm):
    """ Extends and customizes django-allauth sign up form """
    first_name = forms.CharField(
        max_length=30,
        label='First Name',
        widget=forms.TextInput(
            attrs={"placeholder": "First Name", "autocomplete": "First Name"}
        ),
    )
    last_name = forms.CharField(
        max_length=30,
        label='Last Name',
        widget=forms.TextInput(
            attrs={"placeholder": "Last Name", "autocomplete": "Last Name"}
            ),
        )

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user

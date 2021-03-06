from django import forms
from .widgets import ProfileClearableFileInput
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """
    Store information about the user in his/her profile
    """
    class Meta:
        model = UserProfile
        exclude = ('user', 'avatar', 'bio')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_full_name': 'Full Name',
            'default_email': 'Email',
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County',
        }

        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs[
                'class'] = 'border-black rounded-0 profile-form-input'
            self.fields[field].label = False


class UserCustomizedForm(forms.ModelForm):
    """
    Store an avatar image and a short bio about the user
    in his/her profile.
    """
    class Meta:
        model = UserProfile
        exclude = (
            'user',
            'default_full_name',
            'default_email',
            'default_phone_number',
            'default_postcode',
            'default_town_or_city',
            'default_street_address1',
            'default_street_address2',
            'default_county',
            'default_country',
        )
        widgets = {
            'bio': forms.Textarea(attrs={
                'rows': '5',
                'cols': '90',
                'maxlength': '500',
            }),
        }

    avatar = forms.ImageField(
        label='Image', required=False, widget=ProfileClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['bio'].widget.attrs['class'] = 'border-black rounded-0'

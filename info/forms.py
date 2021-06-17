from django import forms


class ContactForm(forms.Form):
    """
    Form that allows users to send a message to the
    website administrators.
    """
    name = forms.CharField(required=True, max_length=100)
    email_address = forms.EmailField(required=True, max_length=150)
    subject = forms.CharField(required=True, max_length=250)
    message = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                'rows': '8',
                'cols': '90',
                'maxlength': '1000',
            },
        ),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Add placeholders
        self.fields['name'].widget.attrs[
            'placeholder'] = 'Write your name here...'
        self.fields['email_address'].widget.attrs[
            'placeholder'] = 'Write your email address here...'
        self.fields['subject'].widget.attrs[
            'placeholder'] = 'Write here, no more than 250 characters'
        self.fields['message'].widget.attrs[
            'placeholder'] = 'Write a message, no more than 1000 characters.'

        # Overwrite the field labels into the Contact Form
        self.fields['name'].label = "Full Name "
        self.fields['email_address'].label = "Email Address "
        self.fields['subject'].label = "Subject "
        self.fields['message'].label = "Message "

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0'

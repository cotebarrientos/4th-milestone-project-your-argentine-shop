from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(required=True, max_length = 100)
    email_address = forms.EmailField(required=True, max_length = 150)
    subject = forms.CharField(required=True, max_length = 250)
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
            
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0'  

      
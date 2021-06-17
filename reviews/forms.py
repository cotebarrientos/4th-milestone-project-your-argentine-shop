from django import forms
from .models import Review


class ReviewCommentForm(forms.ModelForm):
    """
    This form allows users to leave a review about the service
    provided by the online store.
    """
    class Meta:
        model = Review
        fields = ('name', 'email', 'comment', 'rating')
        widgets = {
            'comment': forms.Textarea(attrs={
                'rows': '6',
                'cols': '90',
                'placeholder': 'Comment your review, no more than 1000 char.',
                'maxlength': '1000',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Overwrite the field labels into the Reviews Form
        self.fields['name'].label = "Your Name "
        self.fields['email'].label = "Your Email "
        self.fields['comment'].label = "Your Comment "
        self.fields['rating'].label = "Your Rating "

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0'

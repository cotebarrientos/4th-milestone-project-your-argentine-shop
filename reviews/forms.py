from django import forms
from .models import Review


class ReviewCommentForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('name', 'email', 'comment', 'rating')
        widgets = {
            'comment' : forms.Textarea(attrs={
                'rows': '6',
                'cols': '90',
                'placeholder': 'Comment your review here...',
                'maxlength': '1000',
            }),
            'rating' : forms.Select(attrs={
                'placeholder': 'Select Rating',
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0'    
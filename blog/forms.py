from django import forms
from .widgets import CustomClearableFileInputForPostImage
from .models import Post, Comment


class BlogPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInputForPostImage)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
        widgets = {
            'body' : forms.Textarea(attrs={
                'rows': '6',
                'cols': '90',
                'placeholder': 'Comment here, no more than 1000 characters.',
                'maxlength': '1000',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0'        
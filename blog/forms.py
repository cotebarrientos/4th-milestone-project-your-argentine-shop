from django import forms
from .widgets import CustomClearableFileInputForPostImage
from .models import Post, Comment


class BlogPostForm(forms.ModelForm):
    """
    Form to allow Super User to submit new blogpost
    """
    class Meta:
        model = Post
        fields = '__all__'

    image = forms.ImageField(
        label='Image',
        required=False,
        widget=CustomClearableFileInputForPostImage)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Add placeholders into the Blog Form
        self.fields['title'].widget.attrs[
            'placeholder'] = 'Write here, max 200 char. e.g. Blog Post Title'
        self.fields['slug'].widget.attrs[
            'placeholder'] = 'Write here. max 200 char. e.g. blog-post-title'

        # Set a field as a required field
        self.fields['content'].required = True

        # Overwrite the field labels into the Blog Form
        self.fields['title'].label = "Title "
        self.fields['slug'].label = "Slug "
        self.fields['content'].label = "Content "
        self.fields['author'].label = "Author "
        self.fields['snippet'].label = "Snippet "
        self.fields['status'].label = "Status "

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0'


class CommentForm(forms.ModelForm):
    """
    Form to allow User to submit a comment inside a blogpost
    """
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
        widgets = {
            'body': forms.Textarea(attrs={
                'rows': '6',
                'cols': '90',
                'placeholder': 'Comment here, no more than 1000 characters.',
                'maxlength': '1000',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Overwrite the field labels into the Comment Form
        self.fields['name'].label = "Your Name "
        self.fields['email'].label = "Your Email "
        self.fields['body'].label = "Your Comment "

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0'

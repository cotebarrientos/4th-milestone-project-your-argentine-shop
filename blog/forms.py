from django import forms
from .widgets import CustomClearableFileInputForPostImage
from .models import Post


class BlogPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInputForPostImage)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0'
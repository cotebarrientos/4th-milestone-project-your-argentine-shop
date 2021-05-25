from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        
        # Restrict editing this field within the form
        self.fields['weight_unit'].widget.attrs['readonly'] = True

        # Add placeholders into the Product Form
        self.fields['product_code'].widget.attrs['placeholder'] = 'ALF-12U-CHO-660'
        self.fields['name'].widget.attrs['placeholder'] = 'e.g. Alfajor HAVANNA Chocolate x12 660g'
        self.fields['description'].widget.attrs['placeholder'] = 'Write the product description here ...'
        self.fields['price'].widget.attrs['placeholder'] = '19.50'
        self.fields['weight'].widget.attrs['placeholder'] = '0.660'

        # Categories
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

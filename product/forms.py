from django import forms
from product.models import Product

class  ProductForm(forms.ModelForm):

    class Meta():
        model = Product
        fields = ('name', 'price', 'weight')

        widgets = {
            'name': forms.TextInput(attrs={'class':'textinputclass'}),
            'price':forms.NumberInput(attrs={'class':'numberinputclass'}),
            'weight':forms.NumberInput(attrs={'class':'numberinputclass'}),
        }

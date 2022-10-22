from django.forms import ModelForm
from.models import ProductList

class ProductListForm(ModelForm):
    class Meta:
        model=ProductList
        fields="__all__"

    

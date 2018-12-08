from django import forms
from .models import Item

class AddForm(forms.ModelForm):
    class Meta:
        model = Item
        exclude = ('user','list_date','picture')


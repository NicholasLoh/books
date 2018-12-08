from django import forms
from .models import Profile
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from items.models import Item

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('picture',)

class UserChangeForm(forms.ModelForm):
    first_name = forms.CharField(max_length=200, required = False)
    last_name = forms.CharField(max_length=200, required = False)
    email = forms.CharField(max_length=200, required = False) 
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        password = self.fields.get('password')
        if password:
            password.help_text = password.help_text.format('../password/')
        user_permissions = self.fields.get('user_permissions')
        if user_permissions:
            user_permissions.queryset = user_permissions.queryset.select_related('content_type')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial.get('password')

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        exclude = ('user', 'list_date','picture')

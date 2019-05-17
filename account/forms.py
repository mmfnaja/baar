from django import forms
from .models import staff


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = staff
        fields = ['loginid', 'name','address']


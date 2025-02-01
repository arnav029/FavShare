# forms.py
from django import forms
from .models import FavoriteItem

class FavoriteItemForm(forms.ModelForm):
    class Meta:
        model = FavoriteItem
        fields = ['title', 'type']

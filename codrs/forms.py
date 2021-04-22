from django import forms
from .models import Array, Push

class ArrayForm(forms.ModelForm):

    class Meta:
        model = Array
        fields = ('author', 'body')

class PushForm(forms.ModelForm):

    class Meta:
        model = Push
        fields = ('author', 'body')
# myapp/forms.py

from django import forms

class OrderForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)
    address = forms.CharField(label='Your Address', widget=forms.Textarea)

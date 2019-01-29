from django import forms

class ContactUsForm(forms.Form):
  name = forms.CharField(max_length=10, label='', widget=forms.TextInput(attrs={
    'placeholder': 'Enter ur name'
  }))
  email = forms.EmailField(label='', required=False, widget=forms.EmailInput(attrs={
    'placeholder': 'Enter ur email'
  }))
  description = forms.CharField(max_length=100, label='', widget=forms.Textarea(attrs={
    'placeholder': 'Enter description'
  }))
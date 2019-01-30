from django import forms
from libmgmt.models import Student

class ContactUsForm(forms.Form):
  name = forms.CharField(max_length=10, label='', widget=forms.TextInput(attrs={
    'placeholder': 'Enter ur name'
  }), error_messages={'required': 'Please enter username'})
  email = forms.EmailField(label='', required=False, widget=forms.EmailInput(attrs={
    'placeholder': 'Enter ur email'
  }))
  description = forms.CharField(max_length=100, label='', widget=forms.Textarea(attrs={
    'placeholder': 'Enter description'
  }), error_messages={'required': 'Please enter the description'})

'''class RegisterForm(forms.Form):
  username = forms.CharField(max_length=20, label='', widget=forms.TextInput(attrs={
    'placeholder': 'Enter Username'
  }))
  password = forms.CharField(max_length=10, label='', widget=forms.PasswordInput(attrs={
    'placeholder': 'Enter Password'
  }))
  country = forms.ChoiceField(choices=(('IN', 'India'),('SE', 'South America'),('FR', 'France')))
  gender = forms.ChoiceField(widget=forms.RadioSelect, choices=(('M','Male'),('F', 'Female')))'''

class RegisterForm(forms.ModelForm):
  class Meta:
    model = Student
    fields = ('username', 'password', 'country', 'gender', 'profilepic')

    widgets = {
      'username': forms.TextInput(attrs={
        'placeholder': 'Enter username'
      }),
      'password': forms.PasswordInput(attrs={
        'placeholder': 'Enter password'
      })
    }

    labels = {
      'username': '',
      'password': ''
    }
  
  def __init__(self, *args, **kwargs):
    # TODO: Retrieved countries from database
    countries = (('IN', 'India'), ('AU', 'Australia'))
    gender = (('M','Male'),('F', 'Female'))

    super().__init__(*args, **kwargs)
    self.fields['country'] = forms.ChoiceField(choices=countries)
    self.fields['gender'] = forms.ChoiceField(choices=gender, widget=forms.RadioSelect)
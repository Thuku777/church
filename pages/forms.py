from django import forms
from django.forms import ModelForm

from .models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'required': True, 
                'placeholder': 'Your name...'
            }),
            'email': forms.EmailInput(attrs={
                'required': True, 
                'placeholder': 'Your e-mail...'
            }),
            'message': forms.Textarea(attrs={
                'required': True, 
                'placeholder': 'Say something...'
            }),
        }

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
            'class': 'form-control'})
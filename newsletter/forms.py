from .models import EmailSub, Email
from django import forms

class SubForm(forms.ModelForm):
    class Meta:
        model = EmailSub
        fields = ['first_name', 'last_name', 'em_address']


class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['subject', 'content']
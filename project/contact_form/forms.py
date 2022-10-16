from django import forms


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    number = forms.CharField(max_length=200)
    message = forms.CharField(max_length=1000)
from django import forms

class CreatePersonForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=20)
    last_name = forms.CharField(label='Last name', max_length=30)
    email_address = forms.CharField(label='Email address', max_length=50)

class UpdatePersonForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=20, required=False)
    last_name = forms.CharField(label='Last name', max_length=30, required=False)
    email_address = forms.CharField(label='Email address', max_length=50, required=False)

from django import forms

class add_customer_form(forms.Form):
    name = forms.CharField(max_length=100)
    number = forms.IntegerField()

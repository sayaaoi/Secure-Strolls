from django import forms

class LocationForm(forms.Form):
   start = forms.CharField()
   end = forms.CharField()
from django import forms
import string

class LocationForm(forms.Form):
    start = forms.CharField()
    end = forms.CharField()
    
    # def clean_start(self):
    #     end = self.cleaned_data['end']
    #     punc_check = set(''.join(end))
    #     if len(punc_check.intersection(string.punctuation)) > 0:
    #         raise ValidationError("Address should be formatted <Street Number> <Street Name> <Town> <State>")
            
    #     return end
    
    # def clean_end(self):
    #     start = self.cleaned_data['start']
    #     punc_check = set(''.join(start))
    #     if len(punc_check.intersection(string.punctuation)) > 0:
    #         raise ValidationError("Address should be formatted <Street Number> <Street Name> <Town> <State>")
            
    #     return start
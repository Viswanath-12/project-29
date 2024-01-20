from django import forms

from app.models import *

class StudentForm(forms.ModelForm):
    class Meta():
        model=Student
        fields='__all__'
    
    bot=forms.CharField(max_length=10,required=False,widget=forms.HiddenInput)

    def clean_bot(self):
        b=self.cleaned_data['bot']
        if len(b)>0:
            raise forms.ValidationError('bot found')
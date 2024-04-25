


from django import forms

from .models import *

class TopicForm(forms.ModelForm):   #inherit from Topic class in models.py
    class Meta:
        model = Topic               #ensure the model is in lowercase
        fields = ['text']           #the data, not the field/column name ??
        labels = {'text': 'Text'}   #the field/column name, not the data but ?? 


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': 'Entry'}

        widgets = {'text':forms.Textarea(attrs={'cols':80})}
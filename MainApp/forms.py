


from django import forms

from .models import *

class TopicForm(forms.ModelForm):   #ensure the Model is uppercase
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': 'Text'}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': 'Entry:'}

        widgets = {'text':forms.Textarea(attrs={'cols':80})}
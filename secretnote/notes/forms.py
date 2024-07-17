from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title','text','secret','destruction_date']
        widgets ={
            'title': forms.TextInput(attrs={'class': 'form-control my-3'}),
            'text': forms.Textarea(attrs={'class': 'form-control my-3'}),
            'secret': forms.TextInput(attrs={'class': 'form-control my-3'}),
            'destruction_date': forms.TextInput(attrs={'type':'datetime-local'}),
        }
        labels = {
            'text': "Write your secret note's content",
        }
        
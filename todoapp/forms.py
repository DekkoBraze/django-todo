from django import forms
from .models import *


class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['title', 'content', 'project']
        labels = {
            'title': 'Задача',
            'content': 'Описание',
            'project': 'Проект',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 50, 'rows': 3}),
        }
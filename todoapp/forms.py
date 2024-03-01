from django import forms
from .models import TaksModel

class TaskForm(forms.ModelForm):
    class Meta:
        model = TaksModel
        exclude = ['is_completed']

class EditForm(forms.ModelForm):
    class Meta:
        model = TaksModel
        exclude = ['id']
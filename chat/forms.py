# chat/forms.py
from django import forms

from bootstrap_datepicker_plus.widgets import DateTimePickerInput
class MessageForm(forms.Form):
    content = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Type your message...'}))
    
from django import forms
from .models import Room

class RoomUpdateForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['current_goal', 'next_discussion']  
        
        widgets = {
            "next_discussion": DateTimePickerInput(),
            
        }
  
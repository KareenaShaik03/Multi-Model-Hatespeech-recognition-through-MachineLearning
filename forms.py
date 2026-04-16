
# forms.py
from django import forms

class HateSpeechForm(forms.Form):
    sentence = forms.CharField(
        label='Enter sentence',
        required=False,
        max_length=1000,
        widget=forms.Textarea(attrs={
            'rows': 4,
            'cols': 40,
            'placeholder': 'Enter text OR upload audio...'
        })
    )

    audio = forms.FileField(
        required=False,
        label='Upload Audio (.wav)',
        help_text='Optional: upload audio file'
    )


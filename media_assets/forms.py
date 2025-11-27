from django import forms
from .models import MediaAsset

class MediaAssetForm(forms.ModelForm):
    class Meta:
        model = MediaAsset
        fields = ['title', 'description', 'category_file', 'media_file', 'is_public']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form_control'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form_control',
                'rows': 3
            }),
            'category': forms.Select(attrs={
                'class': 'form_control'              
            }),
            'is_public' : forms.CheckboxInput(attrs={
                'class': 'form_check_input'
            })

        }
from django import forms
from django import forms
from.models import Short_urls

class UrlForm(forms.ModelForm):
    class Meta:
        model= Short_urls  
        fields =['long_url']

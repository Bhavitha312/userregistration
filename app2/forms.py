from django import forms 
from app2.models import user

class loginform(forms.ModelForm):
    class Meta:
        model=user 
        fields=['name','lastname','password']
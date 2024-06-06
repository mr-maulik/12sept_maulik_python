from django import forms
from .models import *


class Apoimentf(forms.ModelForm):
    class Meta:
        model=apoiment
        fields='__all__'

# class newuser(forms.ModelForm):
#     class Meta:
#         model=usersignup
#         fields=['firstname','laststname','gmail','pin']
        
# class updateform(forms.ModelForm):
#     class Meta:
#         model=usersignup
#         fields=['firstname','laststname','profil_img']
        
# class forpass(forms.ModelForm):
#     class Meta:
#         model=usersignup
#         fields=['pin']
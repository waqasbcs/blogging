from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext,gettext_lazy as _
from .models import post



class sigupform(UserCreationForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password (again)',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
     model = User
     fields = ['username','first_name','last_name','email']
     labels = {'email':'Email','first_name':'First_Name','last_name':'Last_Name'}
     widgets = {'username':forms.TextInput(attrs={'class':'form-control'}),
                'first_name':forms.TextInput(attrs={'class':'form-control'}),
                'last_name':forms.TextInput(attrs={'class':'form-control'}),
                'email':forms.EmailInput(attrs={'class':'form-control'}),
     }
class loginform(AuthenticationForm):
 
 username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}))
 password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'form-control'}))

class postform(forms.ModelForm):
     class Meta:
      model = post
      fields = 'title','description'
      widgets = {'title':forms.TextInput(attrs={'class':'form-control'}),
                'description':forms.Textarea(attrs={'class':'form-control'}),}
                
        
         
        
    
    
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model





class RegForm(UserCreationForm):
    email=forms.EmailField(help_text='A valid email is required',required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    
    class Meta:
        model=get_user_model()
        fields=['first_name','last_name','email','username','password1','password2']
        
    def save(self,commit=True):
        user=super(RegForm,self).save(commit=False)
        user.email=self.cleaned_data['email']
        if commit:
            user.save()
        return user
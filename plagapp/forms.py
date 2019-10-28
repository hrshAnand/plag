from django import forms
from plagapp.models import UserProfileInfo
from django.contrib.auth.models import User
from plagapp.models import Document
class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta():
		model = User
		fields = ('email','username','password')
class UserProfileInfoForm(forms.ModelForm):
	class Meta():
		model = UserProfileInfo
		fields = ('portfolio_site','profile_pic')

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )
from django import forms

class FileForm(forms.Form):
    f1 = forms.FileField(required=True)
    f2 = forms.FileField(required=True)


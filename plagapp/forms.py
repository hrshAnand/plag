from django import forms

class FileForm(forms.Form):
    file1 = forms.FileField(required=True)
    file2 = forms.FileField(required=True)


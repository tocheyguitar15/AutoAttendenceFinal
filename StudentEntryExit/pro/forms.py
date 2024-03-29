from django import forms

class registerStudent(forms.Form):
    id = forms.CharField()
    name = forms.CharField()

class getStudentInfo(forms.Form):
    id = forms.CharField()
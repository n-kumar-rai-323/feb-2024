from django import forms
from myapp.models import Student

class ClassRoomForm(forms.Form):
    name = forms.CharField(max_length=20)

class StudentForm(forms.Form):
    name = forms.CharField(max_length=20)
    age = forms.IntegerField()
    department = forms.CharField(max_length=20)



class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name","age","department"]

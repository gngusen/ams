from django import forms
from .models import Attendance

class  AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['service_name', 'adult_males', 'adult_females', 'child_males', 'child_females']
        
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
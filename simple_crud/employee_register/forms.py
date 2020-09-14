from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('fullname', 'contact_no', 'emp_code', 'position')
        labels = {
            'fullname' : 'Full Name',
            'contact_no': 'Contact Number',
            'emp_code' : 'Employee Code',
            'position' : 'Position'
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select Position"


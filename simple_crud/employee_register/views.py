from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee

def employee_list(request):
    data = {'employees' : Employee.objects.all()}
    return render(request, 'employee_register/employee_list.html', data)


def employee_form(request, id = 0):
    if request.method == 'GET':
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk = id)
            form = EmployeeForm(instance = employee)
        return render(request, 'employee_register/employee_form.html', {'form' : form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk = id)
            form = EmployeeForm(request.POST, instance = employee)
        if form.is_valid():
            form.save()
        return redirect('index')


def employee_delete(request, id):
    Employee.objects.get(pk = id).delete()
    return redirect('index')

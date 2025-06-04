from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm

def index (request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
        else:
            form = EmployeeForm()
            user_list = Employee.objects.all()

        context ={
            "user_list": user_list,
            "form" : form
        }
        return render(request, 'myapp/index.html', context)

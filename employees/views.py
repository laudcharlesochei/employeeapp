from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods

from .forms import EmployeeForm
from .models import Employee


def index(request: HttpRequest) -> HttpResponse:
    employees = Employee.objects.all()
    return render(request, "index.html", {"listEmployees": employees})


def show_new_employee_form(request: HttpRequest) -> HttpResponse:
    form = EmployeeForm()
    return render(request, "new_employee.html", {"form": form})


@require_http_methods(["POST"])
def save_employee(request: HttpRequest) -> HttpResponse:
    # Handles both create and update (mirrors Spring controller behaviour)
    form = EmployeeForm(request.POST)
    if form.is_valid():
        employee_id = form.cleaned_data.get("id")
        if employee_id:
            employee = get_object_or_404(Employee, pk=employee_id)
            for field in ("first_name", "last_name", "email"):
                setattr(employee, field, form.cleaned_data[field])
            employee.save()
        else:
            form.save()
        return redirect("employees:index")
    # If invalid, render the same form (best effort)
    template = "update_employee.html" if request.POST.get("id") else "new_employee.html"
    return render(request, template, {"form": form})


def show_form_for_update(request: HttpRequest, id: int) -> HttpResponse:
    employee = get_object_or_404(Employee, pk=id)
    form = EmployeeForm(instance=employee)
    return render(request, "update_employee.html", {"form": form})


def delete_employee(request: HttpRequest, id: int) -> HttpResponse:
    employee = get_object_or_404(Employee, pk=id)
    employee.delete()
    return redirect("employees:index")

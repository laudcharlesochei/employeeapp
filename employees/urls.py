from django.urls import path
from . import views

app_name = "employees"

urlpatterns = [
    path("index", views.index, name="index"),
    path("showNewEmployeeForm", views.show_new_employee_form, name="show_new_employee_form"),
    path("saveEmployee", views.save_employee, name="save_employee"),
    path("showFormForUpdate/<int:id>", views.show_form_for_update, name="show_form_for_update"),
    path("deleteEmployee/<int:id>", views.delete_employee, name="delete_employee"),
]

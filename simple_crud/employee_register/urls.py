from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_list, name = 'index'),
    path('create/', views.employee_form, name = 'create'),
    path('edit/<int:id>/', views.employee_form, name = 'edit'),
    path('delete/<int:id>/', views.employee_delete, name = 'delete')
]

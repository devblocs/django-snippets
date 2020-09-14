from django.urls import path
from . import views

urlpatterns = [
    path('', views.CrudView.as_view(), name = "index"),
    path('user/create/', views.CreateCrudUser.as_view(), name = "create"),
    path('user/update/', views.UpdateCrudUser.as_view(), name = "update"),
    path('user/delete/', views.DeleteCrudUser.as_view(), name = "delete"),
]
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.CrudView.as_view(), name = "index"),
    path('user/', include([
        path('create/', views.CreateCrudUser.as_view(), name = "create"),
        path('update/', views.UpdateCrudUser.as_view(), name = "update"),
        path('delete/', views.DeleteCrudUser.as_view(), name = "delete"),
    ]))
]
from django.shortcuts import render
from django.views.generic import ListView, View
from django.http import JsonResponse
from .models import User

class CrudView(ListView):
    model = User
    template_name = 'crud.html'
    context_object_name = 'users'

class CreateCrudUser(View):
    def post(self, request):
        name = request.POST.get('name', None)
        address = request.POST.get('address', None)
        age = request.POST.get('age', None)

        user = User.objects.create(
            name = name,
            address = address,
            age = age
        )

        userDetails = {
            'id': user.id,
            'name': user.name,
            'address': user.address,
            'age': user.age
        }

        data = {
            'user': userDetails
        }
        return JsonResponse(data)

class UpdateCrudUser(View):
    def  post(self, request):
        id = request.POST.get('id', None)
        name = request.POST.get('name', None)
        address = request.POST.get('address', None)
        age = request.POST.get('age', None)

        obj = User.objects.get(id=id)
        obj.name = name
        obj.address = address
        obj.age = age
        obj.save()

        user = {'id':obj.id, 'name':obj.name, 'address':obj.address, 'age':obj.age}

        data = {
            'user': user
        }
        return JsonResponse(data)

class DeleteCrudUser(View):
    def post(self, request):
        user_id = request.POST.get('id', None)
        User.objects.get(pk = user_id).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)

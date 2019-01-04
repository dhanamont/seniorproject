from django.shortcuts import render, redirect
from django.template import Context, Template

from django.http import HttpResponse

from rolepermissions.decorators import has_role_decorator
from rolepermissions.checkers import has_role
from rolepermissions.roles import get_user_roles

from . import views
from django.views.generic import View
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

User = get_user_model()

# Create your views here.
class HomeView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user = request.user
            if (has_role(user, 'icnurse')):
            	role = "icnurse"
            elif (has_role(user, 'doctor')):
                role = "doctor"
            elif (has_role(user, 'datasci')):
                role = "datasci"

            context = {
                'role' : role,
            }
            return render(request,'home.html',context)
        else:
            return redirect('login')
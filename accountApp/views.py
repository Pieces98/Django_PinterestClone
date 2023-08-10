from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountApp.forms import AccountUpdateForm
from accountApp.models import HelloWorld


# Create your views here.

def hello_world(request):
    if request.method == "POST":
        tmp = request.POST.get('hello_world_input')

        new_hello_world = HelloWorld()
        new_hello_world.text = tmp
        new_hello_world.save()

        return HttpResponseRedirect(reverse('accountApp:hello_world'))
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountApp/hello_world.html', context={'hello_world_list': hello_world_list})

class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountApp:hello_world')
    template_name = 'accountApp/create.html'

class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountApp/detail.html'


class AccountUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountApp:hello_world')
    template_name = 'accountApp/update.html'

class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountApp:login')
    template_name = 'accountApp/delete.html'
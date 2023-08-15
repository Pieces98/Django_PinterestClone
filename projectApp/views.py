from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView

from projectApp.forms import ProjectCreationForm
from projectApp.models import Project


# Create your views here.
@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreationForm
    template_name = 'projects/create.html'

    def get_success_url(self):
        return reverse('projectApp:detail', kwargs={'pk':self.object.pk})

class ProjectDetailView(DetailView):
    model = Project
    context_object_name = 'target_project'
    template_name = 'projects/detail.html'

class ProjectListView(ListView):
    model = Project
    template_name = 'projects/list.html'
    context_object_name = 'project_list'
    paginate_by = 25

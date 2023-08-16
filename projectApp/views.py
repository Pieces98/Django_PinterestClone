from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView
from django.views.generic.list import MultipleObjectMixin

from articleApp.models import Article
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

class ProjectDetailView(DetailView, MultipleObjectMixin):
    model = Project
    context_object_name = 'target_project'
    template_name = 'projects/detail.html'

    paginate_by = 25
    def get_context_data(self, **kwargs):
        object_list = Article.objects.filter(project=self.get_object())
        return super(ProjectDetailView, self).get_context_data(object_list=object_list, **kwargs)

class ProjectListView(ListView):
    model = Project
    template_name = 'projects/list.html'
    context_object_name = 'project_list'
    paginate_by = 25

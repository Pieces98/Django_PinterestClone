from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView

from articleApp.decorators import article_ownership_required
from articleApp.forms import ArticleCreationForm
from articleApp.models import Article


# Create your views here.
@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreationForm
    template_name = 'articleApp/create.html'

    def form_valid(self, form):
        tmp_article = form.save(commit=False)
        tmp_article.writer = self.request.user
        tmp_article.save()

        return super().form_valid(form)
    def get_success_url(self):
        return reverse('articleApp:detail', kwargs={'pk':self.object.pk})

@method_decorator(article_ownership_required, 'get')
@method_decorator(article_ownership_required, 'post')
class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleCreationForm
    template_name = 'articleApp/update.html'
    context_object_name = 'target_article'

    def get_success_url(self):
        return reverse('articleApp:detail', kwargs={'pk':self.object.pk})

class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'target_article'
    template_name = 'articleApp/detail.html'

@method_decorator(article_ownership_required, 'get')
@method_decorator(article_ownership_required, 'post')
class ArticleDeleteView(DeleteView):
    model = Article
    context_object_name = 'target_article'
    template_name = 'articleApp/delete.html'
    success_url = reverse_lazy('articleApp:list')

class ArticleListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'articleApp/list.html'
    paginate_by = 5
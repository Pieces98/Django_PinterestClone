from django.shortcuts import render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView

from articleApp.models import Article
from commentApp.decorators import comment_ownership_required
from commentApp.forms import CommentCreationForm
from commentApp.models import Comment

# Create your views here.
class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreationForm
    template_name = 'commentApp/create.html'

    def form_valid(self, form):
        tmp_comment = form.save(commit=False)
        tmp_comment.article = Article.objects.get(pk=self.request.POST['article_pk'])
        tmp_comment.writer = self.request.user
        tmp_comment.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('articleApp:detail', kwargs={'pk':self.object.article.pk})

@method_decorator(comment_ownership_required, 'get')
@method_decorator(comment_ownership_required, 'post')
class CommentDeleteView(DeleteView):
    model = Comment
    context_object_name = 'target_comment'
    template_name = 'commentApp/delete.html'

    def get_success_url(self):
        return reverse('articleApp:detail', kwargs={'pk': self.object.article.pk})

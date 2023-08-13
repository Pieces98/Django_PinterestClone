from django.urls import path
from django.views.generic import TemplateView

from articleApp.views import ArticleCreateView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView

app_name = 'articleApp'

urlpatterns = [
    path('list/', TemplateView.as_view(template_name='articleApp/list.html'), name='list'),

    path('create/', ArticleCreateView.as_view(template_name='articleApp/create.html'), name='create'),
    path('detail/<int:pk>', ArticleDetailView.as_view(template_name='articleApp/detail.html'), name='detail'),
    path('update/<int:pk>', ArticleUpdateView.as_view(template_name='articleApp/update.html'), name='update'),
    path('delete/<int:pk>', ArticleDeleteView.as_view(template_name='articleApp/delete.html'), name='delete'),

]

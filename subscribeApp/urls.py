from django.urls import path

from projectApp.views import ProjectListView, ProjectCreateView, ProjectDetailView
from subscribeApp.views import SubscriptionView, SubscriptionListView

app_name = 'subscribeApp'

urlpatterns = [
    path('subscribe/', SubscriptionView.as_view(), name='subscribe'),
    path('list/', SubscriptionListView.as_view(), name='list')
]
from django.urls import path

from projectApp.views import ProjectListView, ProjectCreateView, ProjectDetailView
from subscribeApp.views import SubscriptionView

app_name = 'subscribeApp'

urlpatterns = [
    path('subscribe/', SubscriptionView.as_view(), name='subscribe')
]
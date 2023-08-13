from django.urls import path

from profileApp.views import ProfileCreateView

app_name = 'profileApp'

urlpatterns = [
    path('create/', ProfileCreateView.as_view(), name='create')
]
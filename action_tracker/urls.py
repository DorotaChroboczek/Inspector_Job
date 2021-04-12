from django.urls import path

from .views import ActionsView

app_name = 'action_tracker'

urlpatterns = [
    path('', ActionsView.as_view(), name='actions'),
]

from django.views.generic import ListView

from .models import Action


class ActionsView(ListView):
    template_name = 'actions.html'
    model = Action
    context_object_name = 'actions'

    def get_queryset(self):
        return Action.objects.all().order_by('-id')

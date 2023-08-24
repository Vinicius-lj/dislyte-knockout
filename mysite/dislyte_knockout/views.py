from django.views import generic
from django.db.models import Count, F
from .models import Esper, Player, Player_esper

class IndexView(generic.ListView):
    template_name = 'dislyte_knockout/index.html'
    context_object_name = 'most_used_esper'
    def get_queryset(self):
        return Esper.objects.annotate(
            count=Count('player_esper')
        ).order_by('-count')
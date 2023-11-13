from django.views.generic import ListView, TemplateView
from django.db.models import Count
from .models import Esper, Player, Player_esper


class HomePageView(TemplateView):
    template_name = 'dislyte_knockout/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Add most_used_esper data to the context
        context['most_used_esper'] = MostUsedEsperView().get_queryset()

        # Add most_used_class data to the context
        context['most_used_class'] = MostUsedClassView().get_queryset()

        return context


class MostUsedEsperView(ListView):
    model = Esper
    template_name = 'dislyte_knockout/most_used_esper.html'
    context_object_name = 'most_used_esper'

    def get_queryset(self):
        return Esper.objects.annotate(
            # Reverse Relationship: counts how many related objects there are in Player_esper for each object in Esper.
            count=Count('player_esper')
        ).order_by('-count')


class MostUsedClassView(ListView):
    model = Player_esper
    template_name = 'dislyte_knockout/most_used_class.html'
    context_object_name = 'most_used_class'

    def get_queryset(self):
        return Player_esper.objects.values('esper_id__classe').annotate(
            count=Count('esper_id__classe')
        ).order_by('-count')

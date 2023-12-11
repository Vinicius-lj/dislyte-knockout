from django.views.generic import ListView, TemplateView
from django.db.models import Count
from .models import Player_esper

VERSION = '3.3.6'


class HomePageView(TemplateView):
    template_name = 'dislyte_knockout/home.html'

    def get_context_data(self):
        context = super().get_context_data()

        context['most_used_esper'] = MostUsedEsperView().get_queryset()
        context['most_used_class'] = MostUsedClassView().get_queryset()
        context['most_used_role'] = MostUsedRoleView().get_queryset()
        context['most_used_rarity'] = MostUsedRarityView().get_queryset()
        context['most_used_leader_effect'] = MostUsedLeaderEffectView().get_queryset()
        context['ressonance'] = RessonanceView().get_queryset()

        return context


class MostUsedEsperView(ListView):
    model = Player_esper
    template_name = 'dislyte_knockout/most_used_esper.html'
    context_object_name = 'most_used_esper'

    def get_queryset(self):
        condition = {'version': VERSION}
        return list(Player_esper.objects.filter(**condition).values('esper_id__name', 'esper_id__classe').annotate(
            count=Count('esper_id__name')
        ).order_by('-count'))


class MostUsedClassView(ListView):
    model = Player_esper
    template_name = 'dislyte_knockout/chart_class.html'
    context_object_name = 'most_used_class'

    def get_queryset(self):
        condition = {'version': VERSION}
        return list(Player_esper.objects.filter(**condition).values('esper_id__classe').annotate(
            count=Count('esper_id__classe')
        ).order_by('-count'))


class MostUsedRoleView(ListView):
    model = Player_esper
    template_name = 'dislyte_knockout/chart_role.html'
    context_object_name = 'most_used_role'

    def get_queryset(self):
        condition = {'version': VERSION}
        return list(Player_esper.objects.filter(**condition).values('esper_id__role').annotate(
            count=Count('esper_id__role')
        ).order_by('-count'))


class MostUsedRarityView(ListView):
    model = Player_esper
    template_name = 'dislyte_knockout/chart_rarity.html'
    context_object_name = 'most_used_rarity'

    def get_queryset(self):
        condition = {'version': VERSION}
        return list(Player_esper.objects.filter(**condition).values('esper_id__rarity').annotate(
            count=Count('esper_id__rarity')
        ).order_by('-count'))


class MostUsedLeaderEffectView(ListView):
    model = Player_esper
    template_name = 'dislyte_knockout/chart_leader_effect.html'
    context_object_name = 'most_used_leader_effect'

    def get_queryset(self):
        condition = {'ifleader': True, 'version': VERSION}
        return list(Player_esper.objects.filter(**condition).values('esper_id__leader_effect').annotate(
            count=Count('esper_id__leader_effect')
        ).order_by('-count'))


class RessonanceView(ListView):
    model = Player_esper
    template_name = 'dislyte_knockout/chart_ressonance.html'
    context_object_name = 'ressonance'

    def get_queryset(self):
        condition = {'version': VERSION}
        return list(Player_esper.objects.filter(**condition).values('ressonance').annotate(
            count=Count('ressonance')
        ).order_by('ressonance'))

from django.views.generic import ListView, TemplateView
from django.db.models import Count, F, Window, Value, Subquery, OuterRef
from django.db.models.functions import Rank, Coalesce
from .models import Player_esper

CURRENT_VERSION = '3.4.3'
PREVIOUS_VERSION = '3.4.1'


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
        context['guild'] = GuildView().get_queryset()

        return context


class MostUsedEsperView(ListView):
    model = Player_esper
    template_name = 'dislyte_knockout/most_used_esper.html'
    context_object_name = 'most_used_esper'

    def get_queryset(self):
        current_version_queryset = (
            Player_esper.objects
            .filter(version=CURRENT_VERSION)
            .values('esper_id__name')
            .annotate(count=Count('esper_id__name'))
            .annotate(position=Window(expression=Rank(), order_by=F('count').desc()))
        )

        previous_version_queryset = (
            Player_esper.objects
            .filter(version=PREVIOUS_VERSION)
            .values('esper_id__name')
            .annotate(count=Count('esper_id__name'))
            .annotate(position=Window(expression=Rank(), order_by=F('count').desc()))
        )

        ressonance_queries = []
        for i in range(7):
            ressonance_queries.append(Player_esper.objects.filter(version=CURRENT_VERSION, ressonance=i).values(
                'esper_id__name').annotate(ress=Count('esper_id__name')))

        for i, ressonance_query in enumerate(ressonance_queries):
            ressonance_field = f'ress{i}'
            current_version_queryset = current_version_queryset.annotate(**{ressonance_field: Coalesce(Subquery(
                ressonance_query.filter(esper_id__name=OuterRef('esper_id__name')).values('ress')[:1]), Value(0))})

        for esper in current_version_queryset:
            esper['rank_variation'] = self.get_rank_variation(
                esper, previous_version_queryset)

        return list(current_version_queryset)

    def get_rank_variation(self, current_esper, previous_version_queryset):

        for previous_esper in previous_version_queryset:
            if previous_esper['esper_id__name'] == current_esper['esper_id__name']:
                return previous_esper['position'] - current_esper['position']

        return None


class MostUsedClassView(ListView):
    model = Player_esper
    template_name = 'dislyte_knockout/chart_class.html'
    context_object_name = 'most_used_class'

    def get_queryset(self):
        condition = {'version': CURRENT_VERSION}
        return list(Player_esper.objects.filter(**condition).values('esper_id__classe').annotate(
            count=Count('esper_id__classe')
        ).order_by('-count'))


class MostUsedRoleView(ListView):
    model = Player_esper
    template_name = 'dislyte_knockout/chart_role.html'
    context_object_name = 'most_used_role'

    def get_queryset(self):
        condition = {'version': CURRENT_VERSION}
        return list(Player_esper.objects.filter(**condition).values('esper_id__role').annotate(
            count=Count('esper_id__role')
        ).order_by('-count'))


class MostUsedRarityView(ListView):
    model = Player_esper
    template_name = 'dislyte_knockout/chart_rarity.html'
    context_object_name = 'most_used_rarity'

    def get_queryset(self):
        condition = {'version': CURRENT_VERSION}
        return list(Player_esper.objects.filter(**condition).values('esper_id__rarity').annotate(
            count=Count('esper_id__rarity')
        ).order_by('-count'))


class MostUsedLeaderEffectView(ListView):
    model = Player_esper
    template_name = 'dislyte_knockout/chart_leader_effect.html'
    context_object_name = 'most_used_leader_effect'

    def get_queryset(self):
        condition = {'ifleader': True, 'version': CURRENT_VERSION}
        return list(Player_esper.objects.filter(**condition).values('esper_id__leader_effect').annotate(
            count=Count('esper_id__leader_effect')
        ).order_by('-count'))


class RessonanceView(ListView):
    model = Player_esper
    template_name = 'dislyte_knockout/chart_ressonance.html'
    context_object_name = 'ressonance'

    def get_queryset(self):
        condition = {'version': CURRENT_VERSION}
        return list(Player_esper.objects.filter(**condition).values('ressonance').annotate(
            count=Count('ressonance')
        ).order_by('ressonance'))


class GuildView(ListView):
    model = Player_esper
    template_name = 'dislyte_knockout/chart_guild.html'
    context_object_name = 'guild'

    def get_queryset(self):
        condition = {'version': CURRENT_VERSION}
        guild_counts = Player_esper.objects.filter(**condition).values('player_id__guild').annotate(
            count=Count('player_id__guild')/25)

        return list(guild_counts.filter(count__gt=1).order_by('-count'))

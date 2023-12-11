from django.urls import path

from . import views

app_name = 'dislyte_knockout'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('espers/', views.MostUsedEsperView.as_view(), name='most_used_esper'),
    path('class/', views.MostUsedClassView.as_view(), name='most_used_class'),
    path('role/', views.MostUsedRoleView.as_view(), name='most_used_role'),
    path('role/', views.MostUsedRarityView.as_view(), name='most_used_rarity'),
    path('leader_effect/', views.MostUsedLeaderEffectView.as_view(),
         name='most_used_leader_effect'),
    path('ressonance/', views.RessonanceView.as_view(), name='ressonance'),

]

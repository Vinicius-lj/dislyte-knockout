from django.urls import path

from . import views

app_name = 'dislyte_knockout'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('espers/', views.MostUsedEsperView.as_view(), name='most_used_esper'),
    path('class/', views.MostUsedClassView.as_view(), name='most_used_class'),

]

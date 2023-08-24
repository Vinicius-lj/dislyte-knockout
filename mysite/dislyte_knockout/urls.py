from django.urls import path

from . import views

app_name = 'dislyte_knockout'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('queryStatistic', views.queryStatistic),
    path('queryAreaChart', views.queryAreaChart),
    path('queryBarChart', views.queryBarChart),
    path('queryDetails', views.queryDetails),
]

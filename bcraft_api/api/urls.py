from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'^get_stats/(?P<start_date>[\w\-\.]+)/(?P<end_date>[\w\-\.]+)/$', views.GetStatisticsView.as_view()),
    path('send_stats', views.SendStatisticsView.as_view())
]
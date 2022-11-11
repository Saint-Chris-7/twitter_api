from django.urls import path

from fetch.views import TrendView, TimelineView

app_name = "fetch"
urlpatterns = [

    path("",TrendView.as_view(),name="trend-partial"),
    path("timeline/",TimelineView.as_view(),name="timeline-partial"),
]
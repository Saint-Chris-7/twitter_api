from django.urls import path

from fetch.views import TrendView, TimelineView, IndexView

app_name = "fetch"
urlpatterns = [
    path("",IndexView.as_view(),name="index-page"),
    path("trends/",TrendView.as_view(),name="trend-partial"),
    path("timeline/",TimelineView.as_view(),name="timeline-partial"),
]
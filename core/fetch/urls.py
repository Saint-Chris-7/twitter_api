from django.urls import path

from fetch.views import index, DemoTemplate

app_name = "fetch"
urlpatterns = [
    path("",index,name="index-page"),
    path("demo/",DemoTemplate.as_view(),name="demo-page"),
]
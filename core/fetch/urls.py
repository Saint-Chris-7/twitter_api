from django.urls import path

from fetch.views import index

app_name = "fetch"
urlpatterns = [
    path("",index,name="index-page"),
]
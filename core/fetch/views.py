from django.shortcuts import render
from django.views.generic.base import TemplateView

from .tasks import search_country_trend
# Create your views here.


def index(request,*args,**kwargs):
    results = search_country_trend.delay()
    return render(request,"index.html",{"results":results})
    


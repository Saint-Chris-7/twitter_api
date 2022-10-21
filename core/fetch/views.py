from django.shortcuts import render
from django.views.generic.base import TemplateView

from .tasks import search_country_trend
# Create your views here.

class DemoTemplate(TemplateView):
    template_name = "demo.html"

def index(request,*args,**kwargs):
    # results = search_country_trend.delay()
    results = "hello world"
    return render(request,"index.html",{"results":results})
    


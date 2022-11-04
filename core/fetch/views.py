from typing import Any, Dict
from django.shortcuts import render
from django.views.generic.base import TemplateView

from .tasks import my_timeline, global_trends
from .timeline import my_timeline
from .trends import global_trends
# Create your views here.

class DemoTemplate(TemplateView):
    template_name = "trends.html"
    
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["trendings"] = global_trends.delay()
        return context

def index(request,*args,**kwargs):
    pass
    # results = search_country_trend.delay()
    tweets = my_timeline()
    # results = {}
    # for tweet in tweets:

    return render(request,"index.html",{"tweets":tweets})

def trends(request,*args,**kwargs):
    return render(request,"demo.html")
    


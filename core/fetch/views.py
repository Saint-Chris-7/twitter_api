from typing import Any, Dict
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT

# from .tasks import my_timeline, global_trends
from .timeline import my_timeline
from .trends import global_trends


class IndexView(TemplateView):
    template_name = "base.html"

CACHE_TTL = getattr(settings,"CACHE_TTL",DEFAULT_TIMEOUT)
method_decorator(cache_page(CACHE_TTL),name="dispatch")
class TrendView(TemplateView):
    template_name = "trends.html"
    
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["trendings"] = global_trends()
        print(context["trendings"])
        return context


CACHE_TTL = getattr(settings,"CACHE_TTL",DEFAULT_TIMEOUT)
method_decorator(cache_page(CACHE_TTL),name="dispatch")
class TimelineView(TemplateView):
    """ Timeline view """

    template_name = "timeline.html"
    
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["tweets"] = my_timeline()
        return context




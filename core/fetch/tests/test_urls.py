from symbol import import_from
from django.test import TestCase,SimpleTestCase
from django.urls import resolve,reverse#path has to resolve to a view
from fetch.views import index, DemoTemplate

class TestUrls(SimpleTestCase):#simpletestcase is used when there is no need to interact with the database
    def test_index_url_resolved(self):
        url = reverse("fetch:index-page")
        self.assertEqual(resolve(url).func,index)
    
    def test_demo_url_resolved(self):
        url = reverse("fetch:demo-page")
        self.assertEqual(resolve(url).func.view_class,DemoTemplate)
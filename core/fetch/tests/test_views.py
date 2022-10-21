from django.test import TestCase, Client
from django.urls import reverse

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
    
    def test_index_view(self):
        response = self.client.get(reverse("fetch:index-page"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,"index.html")



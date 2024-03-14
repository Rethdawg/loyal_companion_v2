from django.test import TestCase
from django.urls import reverse


# Create your tests here.
class IndexViewTests(TestCase):
    def test_dashboard_view(self):
        """
        Testing to see if the dashboard page responds with OK when reversed from herald-index.
        :return:None
        """
        self.response_nc = self.client.get(reverse('herald-index'))  # No context response
        self.assertEqual(self.response_nc.status_code, 200, 'Page unreachable.')



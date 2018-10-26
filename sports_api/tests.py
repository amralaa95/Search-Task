from django.test import TestCase
from django.core.urlresolvers import reverse
import json
# Create your tests here.
class HomeViewTest(TestCase):
    def test_homepage(self):
        """
        Test that tests valid retreival of homepage
        """
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
    

    def test_success_search(self):
        '''
        Test AJAX submission of valid data
        '''
        response = self.client.post(reverse('sports_api:search'),
                                    {'text': 'جوو',},
                                    HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        self.assertEqual(json.loads(response.content)['message'],
                         "Successfully submitted form data.")




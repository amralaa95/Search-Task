from django.test import TestCase
from django.urls import reverse
import json
# Create your tests here.
class HomeViewTest(TestCase):
    def test_homepage(self):
        """
        Test that tests valid redirect of homepage
        """
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
    

    def test_form_success_ajax(self):
        '''
        Test AJAX submission of empty data
        '''
        response = self.client.get(reverse('sports_api:search'),
                                    {},
                                    HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code,200)

    def test_success_search(self):
        '''
        Test AJAX submission of existing data
        '''
        response = self.client.get(reverse('sports_api:search'),
                                    {'text':'صلاح'},
                                    HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"صلاح")



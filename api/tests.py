from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from api.models import Quote


BASE_URL = 'https://localhost:8000/api/'
payload = {
            'quote_author': 'Nelson Mandela',
            'quote_body': 'Do not judge me by my successes, judge me by how many times I fell down and got back up again.',
            'context': 'Innaugural Speech',
            'source': '2020'
        }

class QuoteModelTest(APITestCase):
    
    def test_create_model(self):
        ''' test that a quote is successfully created '''
        quote_author = 'Nelson Mandela'
        quote_body = 'Do not judge me by my successes, judge me by how many times I fell down and got back up again.'
        context = 'Innaugural Speech'
        source = '2020'

        quote = Quote(quote_author=quote_author, quote_body=quote_body, source=source, context=context)
        quote.save()
        self.assertEqual(quote.source, '2020')
        self.assertEqual(quote.quote_author, 'Nelson Mandela')


class EndpointTest(APITestCase):

    def setUp(self):
        self.client = APIClient()

    def test_post_quote(self):
        ''' test that create a post endpoint is working properly'''
        response = self.client.post(BASE_URL + 'quotes', payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_quote(self):
        '''' test that a user can get a list of all the quotes '''
        response = self.client.get(BASE_URL + 'quotes')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_quote(self):
        ''' test that a quote can be selected by its ID '''
        post_quote = self.client.post(BASE_URL + 'quotes', payload)
        id = post_quote.data['data']['quotes']['id']
        
        response = self.client.get(BASE_URL + 'quotes/' + id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_quote(self):
        ''' test that a quote can be edited '''
        post_quote = self.client.post(BASE_URL + 'quotes', payload)
        id = post_quote.data['data']['quotes']['id']
        
        response = self.client.patch(BASE_URL + 'quotes/' + id, {'quote_author': 'Barrack Obama'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_quote(self):
        ''' test that a quote can be deleted using its ID '''
        post_quote = self.client.post(BASE_URL + 'quotes', payload)
        id = post_quote.data['data']['quotes']['id']

        response = self.client.delete(BASE_URL + 'quotes/' + id)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

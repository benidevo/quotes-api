from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from api.models import Quote


BASE_URL = 'https://localhost:8000/api/'
class QouteModelTest(APITestCase):
    
    def test_creat_model(self):
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
        payload = {
            'quote_author': 'Nelson Mandela',
            'quote_body': 'Do not judge me by my successes, judge me by how many times I fell down and got back up again.',
            'context': 'Innaugural Speech',
            'source': '2020'
        }
        response = self.client.post(BASE_URL + 'quotes', payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


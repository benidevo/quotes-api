from rest_framework.test import APITestCase

class Sample(APITestCase):

    def test_setup(self):
        self.assertEqual(4, 2 + 2)

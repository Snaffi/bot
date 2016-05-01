import json

from django.core.urlresolvers import reverse
from django.test import TestCase, Client

# Create your tests here.
class UserListTestCase(TestCase):

    def test_create_client(self):
        client = Client()
        response = client.post(
            reverse('user_list'),
            data=json.dumps(dict()),
            content_type='application/json',
        )
        self.assertEqual(400, response.status_code)

        response = client.post(
            reverse('user_list'),
            data=json.dumps(dict(
                username='sk',
            )),
            content_type='application/json',
        )
        self.assertEqual(400, response.status_code)


        response = client.post(
            reverse('user_list'),
            data=json.dumps(dict(
                username='sk',
                password='12345',
                email='bbb@ss.ru',
                first_name='first_name',
                last_name='last_name',
            )),
            content_type='application/json',
        )
        self.assertEqual(200, response.status_code)

        response = client.post(
            reverse('user_list'),
            data=json.dumps(dict(
                username='sk',
                password='12345',
                email='bbb@ss.ru',
                first_name='first_name',
                last_name='last_name',
            )),
            content_type='application/json',
        )
        self.assertEqual(400, response.status_code)

        response = client.post(
            reverse('user_list'),
            data=json.dumps(dict(
                username='sk123123',
                password='12345',
                email='bbb@ss.ru',
                first_name='first_name',
                last_name='last_name',
            )),
            content_type='application/json',
        )
        self.assertEqual(400, response.status_code)

        response = client.post(
            reverse('auth'),
            data=json.dumps(dict(
                username='sk',
                password='12345',
            )),
            content_type='application/json',
        )
        self.assertEqual(200, response.status_code)

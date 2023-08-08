from django.test import Client
from django.test import TestCase


class OpenViewsTest(TestCase):

    def setUp(self):
        self.client = Client

    def test_statuses(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/prices/')
        self.assertEqual(response.status_code, 200)

    def test_login_required(self):
        DeliveryUser.objects.create_user(username='test_user', email='test@test.com', password='test_password')

        response = self.client.get('/client_list/')
        self.assertEqual(response.status_code, 302)

        c.login(username='fred', password='secret')

        response = self.client.get('/client_list/')
        self.assertEqual(response.status_code, 200)

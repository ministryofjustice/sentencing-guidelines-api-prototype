from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from sentencing_guidelines_api.api import models
from datetime import date

class AccountTests(APITestCase):
    def test_list_offence(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('offence-list')

        offense = models.Offence(offence_name='test')
        offense.save()

        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.json(),
            {'count': 1, 'next': None, 'previous': None, 'results': [{'offence_name': 'test', 'effective_from': None}]}
        )

    def test_no_offences(self):
        url = reverse('offence-list')

        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.json(),
            {'count': 0, 'next': None, 'previous': None, 'results': []}
        )

    def test_multiple_offences(self):
        url = reverse('offence-list')

        offense = models.Offence(offence_name='test 1')
        offense.save()

        offense = models.Offence(offence_name='test 2', effective_from=date(2020, 1, 1))
        offense.save()

        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.json(),
            {'count': 2, 'next': None, 'previous': None, 'results': [
                {'offence_name': 'test 1', 'effective_from': None },
                {'offence_name': 'test 2', 'effective_from': '2020-01-01'}
            ]}
        )
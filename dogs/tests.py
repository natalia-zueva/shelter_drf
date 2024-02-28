from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from dogs.models import Breed, Dog


class DogTestCase(APITestCase):

    def setUp(self) -> None:
        self.breed = Breed.objects.create(
            name='breed_test'
        )

        self.dog = Dog.objects.create(
            name='dog_test',
            breed=self.breed
        )

    def test_get_list_dogs(self):
        """Test for getting list of dogs"""

        response = self.client.get(
            reverse('dogs:dog_list')
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
    {
                'count': 1,
                'next': None,
                'previous': None,
                'results': [
                    {
                        'name': self.dog.name,
                        'breed': self.dog.breed
                    }
                ]
            }
        )

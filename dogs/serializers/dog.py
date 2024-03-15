import requests
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.relations import SlugRelatedField

from dogs.models import Dog, Breed
from dogs.serializers.breed import BreedDetailSerializer
from dogs.validators import validator_scam_words


class DogSerializer(serializers.ModelSerializer):
    name = serializers.CharField(validators=[validator_scam_words])

    class Meta:
        model = Dog
        fields = '__all__'


class DogListSerializer(serializers.ModelSerializer):
    breed = SlugRelatedField(slug_field='name', queryset=Breed.objects.all())

    class Meta:
        model = Dog
        fields = ('name', 'breed')


class DogDetailSerializer(serializers.ModelSerializer):
    breed = BreedDetailSerializer()
    dog_with_same_breed = SerializerMethodField()
    price_eur = SerializerMethodField()
    price_usd = SerializerMethodField()

    def get_dog_with_same_breed(self, dog):
        return Dog.objects.filter(breed=dog.breed).count()

    def get_price_eur(self, dog):
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=EUR&from=RUB&amount={dog.price}"

        payload = {}
        headers = {
            "apikey": "KOLTaX65l5HYLq35CqiA5407DewGlVpy"
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        result = response.json()
        return result.get("result")

    def get_price_usd(self, dog):
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=USD&from=RUB&amount={dog.price}"

        payload = {}
        headers = {
            "apikey": "KOLTaX65l5HYLq35CqiA5407DewGlVpy"
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        result = response.json()
        return result.get("result")


    class Meta:
        model = Dog
        fields = ('name', 'breed', 'dog_with_same_breed', 'price_eur', 'price_usd')
        
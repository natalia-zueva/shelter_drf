from rest_framework.viewsets import ModelViewSet

from dogs.models import Breed
from dogs.serializers.breed import *


class BreedViewSet(ModelViewSet):
    queryset = Breed.objects.all()
    default_serializer = BreedSerializer
    serializers = {
        'list': BreedListSerializer,
        'retrieve': BreedDetailSerializer,
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)



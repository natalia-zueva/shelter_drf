from rest_framework.generics import RetrieveAPIView, DestroyAPIView, CreateAPIView, UpdateAPIView, ListAPIView

from dogs.models import Dog
from dogs.serializers.dog import DogSerializer


class DogDetailView(RetrieveAPIView):
    serializer_class = DogSerializer
    queryset = Dog.objects.all()


class DogListView(ListAPIView):
    serializer_class = DogSerializer
    queryset = Dog.objects.all()


class DogCreateView(CreateAPIView):
    serializer_class = DogSerializer
    queryset = Dog.objects.all()


class DogUpdateView(UpdateAPIView):
    serializer_class = DogSerializer
    queryset = Dog.objects.all()


class DogDeleteView(DestroyAPIView):
    serializer_class = DogSerializer
    queryset = Dog.objects.all()


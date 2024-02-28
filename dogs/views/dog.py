from rest_framework.generics import RetrieveAPIView, DestroyAPIView, CreateAPIView, UpdateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from dogs.models import Dog
from dogs.permissions import IsModerator, IsDogOwner, IsDogPublic
from dogs.serializers.dog import DogSerializer, DogListSerializer, DogDetailSerializer


class DogDetailView(RetrieveAPIView):
    serializer_class = DogDetailSerializer
    queryset = Dog.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsDogOwner | IsDogPublic]


class DogListView(ListAPIView):
    serializer_class = DogListSerializer
    queryset = Dog.objects.all()
    permission_classes = [IsAuthenticated]


class DogCreateView(CreateAPIView):
    serializer_class = DogSerializer
    queryset = Dog.objects.all()
    permission_classes = [IsAuthenticated]


class DogUpdateView(UpdateAPIView):
    serializer_class = DogSerializer
    queryset = Dog.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsDogOwner]


class DogDeleteView(DestroyAPIView):
    serializer_class = DogSerializer
    queryset = Dog.objects.all()
    permission_classes = [IsAuthenticated, IsDogOwner]


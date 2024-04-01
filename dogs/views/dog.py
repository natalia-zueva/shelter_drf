from django.shortcuts import get_object_or_404
from rest_framework.generics import RetrieveAPIView, DestroyAPIView, CreateAPIView, UpdateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from dogs.models import Dog
from dogs.paginators import DogPaginator
from dogs.permissions import IsModerator, IsDogOwner, IsDogPublic
from dogs.serializers.dog import DogSerializer, DogListSerializer, DogDetailSerializer
from dogs.tasks import send_message_about_like
from users.models import User


class DogDetailView(RetrieveAPIView):
    serializer_class = DogDetailSerializer
    queryset = Dog.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsDogOwner | IsDogPublic]


class DogListView(ListAPIView):
    serializer_class = DogListSerializer
    queryset = Dog.objects.all()
    # permission_classes = [IsAuthenticated]
    pagination_class = DogPaginator


class DogCreateView(CreateAPIView):
    serializer_class = DogSerializer
    queryset = Dog.objects.all()
    # permission_classes = [IsAuthenticated]


class DogUpdateView(UpdateAPIView):
    serializer_class = DogSerializer
    queryset = Dog.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsDogOwner]


class DogDeleteView(DestroyAPIView):
    serializer_class = DogSerializer
    queryset = Dog.objects.all()
    permission_classes = [IsAuthenticated, IsDogOwner]


class SetLikeToDog(APIView):

    def post(self, request):
        print(request.data)
        user = get_object_or_404(User, pk=request.data.get("user"))
        dog = get_object_or_404(Dog, pk=request.data.get("dog"))
        if dog.likes.filter(id=user.id).exists():
            return Response({"result": f"У собаки {dog} уже есть лайк от {user}"}, status=200)
        send_message_about_like.delay(user.username)
        dog.likes.add(user)
        return Response({"result": f"Лайк добавлен для {dog} от {user}"}, status=200)



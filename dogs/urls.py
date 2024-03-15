from django.urls import path
from rest_framework import routers

from dogs.apps import DogsConfig
from dogs.views.breed import *
from dogs.views.dog import *

app_name = DogsConfig.name


urlpatterns = [
    path('', DogListView.as_view(), name='dog_list'),
    path('<int:pk>/', DogDetailView.as_view(), name='dog_detail'),
    path('<int:pk>/update/', DogUpdateView.as_view(), name='dog_update'),
    path('create/', DogCreateView.as_view(), name='dog_create'),
    path('<int:pk>/delete/', DogDeleteView.as_view(), name='dog_delete'),

    path('set_like/', SetLikeToDog.as_view(), name='set_like'),
]

router = routers.SimpleRouter()
router.register('breed', BreedViewSet)

urlpatterns += router.urls
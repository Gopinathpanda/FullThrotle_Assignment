from .models import User, ActivityPeriods
from .serializers import UserSerializer, ActivitySerializer
from rest_framework import generics


# Create your views here.

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ActivityListView(generics.ListAPIView):
    queryset = ActivityPeriods.objects.all()
    serializer_class = ActivitySerializer


class ActivityDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ActivityPeriods.objects.all()
    serializer_class = ActivitySerializer

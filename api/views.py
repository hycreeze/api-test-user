from rest_framework import viewsets
from api.models import User
from api.serializers import UserSerializer


class GetAllUsers(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-created_date')
    serializer_class = UserSerializer


# User view sets.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-updated_date')
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        print(serializer)

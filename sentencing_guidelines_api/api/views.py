from django.contrib.auth.models import User, Group
from .models import Offence
from rest_framework import viewsets
from sentencing_guidelines_api.api.serializers import UserSerializer, GroupSerializer, OffenceSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class OffenceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Offence.objects.all()
    serializer_class = OffenceSerializer


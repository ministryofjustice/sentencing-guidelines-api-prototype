from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Offence


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class OffenceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Offence
        fields = ('offence_name',)
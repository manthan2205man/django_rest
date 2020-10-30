from django.contrib.auth.models import User
from . models import *

from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
     class Meta:
         model = User
         fields = ('id', 'username', 'first_name', 'last_name', 'email')

class MarksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marksmodel
        fields = "__all__"

class StudentSerializer(serializers.ModelSerializer):
    marks=MarksSerializer(read_only=True,many=True)
    class Meta:
        model = Studentmodel
        fields = "__all__"


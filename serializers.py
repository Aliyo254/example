from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'is_elder']


class ElderSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {'password': {'write_only': True}}

    def save(self, **kwargs):
        user = User(
            username=self.validated_data['username'], email=self.validated_data['email'])
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({"error": "password mismatch"})
        user.set_password(password)
        user.is_elder = True
        user.save()
        Elder.objects.create(user=user)
        return user


class ResidentSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {'password': {'write_only': True}}

    def save(self, **kwargs):
        user = User(
            username=self.validated_data['username'], email=self.validated_data['email'])
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({"error": "password mismatch"})
        user.set_password(password)
        user.is_elder = False
        user.save()
        Resident.objects.create(user=user)
        return user


class ControllerSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {'password': {'write_only': True}}

    def save(self, **kwargs):
        user = User(
            username=self.validated_data['username'], email=self.validated_data['email'])
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({"error": "password mismatch"})
        user.set_password(password)
        user.is_elder = False
        user.save()
        Controller.objects.create(user=user)
        return user


class HoodSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Hood
        fields = ('id', 'name', 'location',
                  'about', 'photo')
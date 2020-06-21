from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from django.contrib.auth.models import User
from .models import *

class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = ('username','email' )
        validators = [
            UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=('username','email')
            )
        ]


class SimranSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        temp = NeedSimran.objects.create(**validated_data)
        return temp

    class Meta:
        model = NeedSimran
        fields = ('title','desc')

class HelpSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        temp = NeedHelp.objects.create(**validated_data)
        return temp

    class Meta:
        model = NeedHelp
        fields = ('title','desc')

class AdviceSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        temp = NeedAdvice.objects.create(**validated_data)
        return temp

    class Meta:
        model = NeedAdvice
        fields = ('title','desc')

class IdeaSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        temp = ProjectIdea.objects.create(**validated_data)
        return temp

    class Meta:
        model = ProjectIdea
        fields = ('title','desc','prob')






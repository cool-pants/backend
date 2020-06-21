from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth.models import User
from .models import NeedSimran, NeedHelp, NeedAdvice, ProjectIdea
from .serializers import UserSerializer, SimranSerializer, HelpSerializer, AdviceSerializer, IdeaSerializer

class UserView(APIView):

	permission_classes = [IsAdminUser]

	def get(self, format=None):
		users = User.objects.all()
		serializer = UserSerializer(users, many=True)
		return Response(serializer.data)
		
	def post(self, request):
		serializer = UserSerializer(data=request.data)
		if serializer.is_valid(raise_exception=ValueError):
			serializer.create(validated_data=request.data)
			return Response(
				serializer.data,
				status=status.HTTP_201_CREATED
			)
		return Response(
			{
				"error": True,
				"error_msg": serializer.error_messages,
			},
			status=status.HTTP_400_BAD_REQUEST
		)

		#serializer = serializers.BlogSerializer(data=request.data)

#		if serializer.is_valid():	

class SimranView(APIView):

	def get(self, format=None):
		users = NeedSimran.objects.all()
		serializer = SimranSerializer(users, many=True)
		return Response(serializer.data)
		
	def post(self, request):
		serializer = SimranSerializer(data=request.data)
		if serializer.is_valid(raise_exception=ValueError):
			serializer.create(validated_data=request.data)
			return Response(
				serializer.data,
				status=status.HTTP_201_CREATED
			)
		return Response(
			{
				"error": True,
				"error_msg": serializer.error_messages,
			},
			status=status.HTTP_400_BAD_REQUEST
		)

class HelpView(APIView):

	def get(self, format=None):
		users = NeedHelp.objects.all()
		serializer = HelpSerializer(users, many=True)
		return Response(serializer.data)
		
	def post(self, request):
		serializer = HelpSerializer(data=request.data)
		if serializer.is_valid(raise_exception=ValueError):
			serializer.create(validated_data=request.data)
			return Response(
				serializer.data,
				status=status.HTTP_201_CREATED
			)
		return Response(
			{
				"error": True,
				"error_msg": serializer.error_messages,
			},
			status=status.HTTP_400_BAD_REQUEST
		)

class AdviceView(APIView):

	def get(self, format=None):
		users = NeedAdvice.objects.all()
		serializer = AdviceSerializer(users, many=True)
		return Response(serializer.data)
		
	def post(self, request):
		serializer = AdviceSerializer(data=request.data)
		if serializer.is_valid(raise_exception=ValueError):
			serializer.create(validated_data=request.data)
			return Response(
				serializer.data,
				status=status.HTTP_201_CREATED
			)
		return Response(
			{
				"error": True,
				"error_msg": serializer.error_messages,
			},
			status=status.HTTP_400_BAD_REQUEST
		)
class IdeaView(APIView):

	def get(self, format=None):
		users = ProjectIdea.objects.all()
		serializer = IdeaSerializer(users, many=True)
		return Response(serializer.data)
		
	def post(self, request):
		serializer = ProjectIdea(data=request.data)
		if serializer.is_valid(raise_exception=ValueError):
			serializer.create(validated_data=request.data)
			return Response(
				serializer.data,
				status=status.HTTP_201_CREATED
			)
		return Response(
			{
				"error": True,
				"error_msg": serializer.error_messages,
			},
			status=status.HTTP_400_BAD_REQUEST
		)

from django.urls import path,include
from .views import UserView, SimranView, HelpView, AdviceView, IdeaView
from rest_framework import routers


urlpatterns = [
	path('user/', UserView.as_view(), name ='users'),
	path('simran/', SimranView.as_view(), name ='NeedSimran'),
	path('help/', HelpView.as_view(), name ='NeedHelp'),
	path('advice/', AdviceView.as_view(), name ='NeedAdvice'),
	path('idea/', IdeaView.as_view(), name ='ProjectIdea'),
]